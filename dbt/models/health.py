from datetime import datetime

from amora.models import AmoraModel
from sqlmodel import Field, MetaData


class Health(AmoraModel, table=True):
    id: int = Field(primary_key=True)
    type: str
    sourceName: str
    sourceVersion: str
    unit: str
    creationDate: datetime
    startDate: datetime
    endDate: datetime
    value: float
    device: str

    metadata = MetaData(schema="stg-tau-rex.diogo", quote_schema=True)
