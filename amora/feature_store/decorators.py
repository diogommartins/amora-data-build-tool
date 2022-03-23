from datetime import datetime

import sqlmodel
from feast import ValueType, FeatureView, Feature, BigQuerySource
from google.protobuf.duration_pb2 import Duration
from sqlalchemy.sql import sqltypes

from amora.feature_store.config import settings
from amora.feature_store.registry import FEATURE_REGISTRY
from amora.feature_store.protocols import FeatureViewSourceProtocol
from amora.models import Model
from amora.providers.bigquery import get_fully_qualified_id

PYTHON_TYPES_TO_FS_TYPES = {
    sqltypes.Float: ValueType.FLOAT,
    sqltypes.String: ValueType.STRING,
    sqlmodel.AutoString: ValueType.STRING,
    sqltypes.Integer: ValueType.INT64,
    bytes: ValueType.BYTES,
    sqltypes.Boolean: ValueType.BOOL,
    sqltypes.Date: ValueType.UNIX_TIMESTAMP,
    sqltypes.DateTime: ValueType.UNIX_TIMESTAMP,
}


def feature_view(model: Model):
    if not isinstance(model, FeatureViewSourceProtocol):
        raise ValueError(
            f"Feature view models must implement the "
            f"{FeatureViewSourceProtocol.__name__} protocol. "
            f"{model} failed the check"
        )

    FEATURE_REGISTRY[model] = FeatureView(
        name=model.unique_name,
        entities=[col.name for col in model.feature_view_entities()],
        features=[
            Feature(
                name=col.name,
                dtype=PYTHON_TYPES_TO_FS_TYPES[col.type.__class__],
            )
            for col in model.feature_view_features()
        ],
        batch_source=BigQuerySource(table_ref=get_fully_qualified_id(model)),
        ttl=Duration(seconds=settings.DEFAULT_FEATURE_TTL_IN_SECONDS),
    )

    return model
