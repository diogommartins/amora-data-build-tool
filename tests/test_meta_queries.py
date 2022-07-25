import pytest

from amora.meta_queries import summarize, summarize_column

from tests.models.array_repeated_fields import ArrayRepeatedFields
from tests.models.health import Health
from tests.models.step_count_by_source import StepCountBySource


@pytest.fixture(scope="module")
def health_model_summary():
    return [
        {
            "column_name": "creationDate",
            "column_type": "DATETIME",
            "min": "2019-12-09 13:47:53+00",
            "max": "2021-07-23 03:14:19+00",
            "avg": None,
            "unique_count": 537208,
            "null_percentage": 0.0,
            "stddev": None,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "startDate",
            "column_type": "DATETIME",
            "min": "2019-12-08 09:48:52+00",
            "max": "2021-07-23 03:14:19+00",
            "avg": None,
            "unique_count": 878421,
            "null_percentage": 0.0,
            "stddev": None,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "endDate",
            "column_type": "DATETIME",
            "min": "2019-12-08 09:49:32+00",
            "max": "2021-07-23 03:14:19+00",
            "avg": None,
            "unique_count": 878606,
            "null_percentage": 0.0,
            "stddev": None,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "id",
            "column_type": "INTEGER",
            "min": "0",
            "max": "1050052",
            "avg": "525025.99999996088",
            "unique_count": 1050053,
            "null_percentage": 0.0,
            "stddev": 303124.3354442229,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "type",
            "column_type": "VARCHAR",
            "min": "ActiveEnergyBurned",
            "max": "WalkingStepLength",
            "avg": None,
            "unique_count": 15,
            "null_percentage": 0.0,
            "stddev": None,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "sourceName",
            "column_type": "VARCHAR",
            "min": "Diogo iPhone",
            "max": "iPhone",
            "avg": None,
            "unique_count": 4,
            "null_percentage": 0.0,
            "stddev": None,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "sourceVersion",
            "column_type": "VARCHAR",
            "min": "12.0.1",
            "max": "202106210942",
            "avg": None,
            "unique_count": 25,
            "null_percentage": 0.0,
            "stddev": None,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "unit",
            "column_type": "VARCHAR",
            "min": "%",
            "max": "km/hr",
            "avg": None,
            "unique_count": 10,
            "null_percentage": 0.3585007005625527,
            "stddev": None,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "value",
            "column_type": "FLOAT",
            "min": "0",
            "max": "1742",
            "avg": "82.164803980394083",
            "unique_count": 8101,
            "null_percentage": 0.0,
            "stddev": 37.98340562839273,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "device",
            "column_type": "VARCHAR",
            "min": "<<HKDevice: 0x282200190>, name:Mi Smart Band 4, hardware:V0.25.17.5, software:V1.0.9.66, localIdentifier:3C779DE0-B720-D2F6-47B2-51F4DFC484BF>",
            "max": "<<HKDevice: 0x28229ff70>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone12,5, software:14.4.2>",
            "avg": None,
            "unique_count": 423,
            "null_percentage": 61.58241210360449,
            "stddev": None,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
    ]


def test_summarize(health_model_summary):
    summary = summarize(Health)
    assert summary.to_dict(orient="records") == health_model_summary


@pytest.fixture(scope="module")
def step_count_by_source_model_summary():
    return [
        {
            "column_name": "event_timestamp",
            "column_type": "TIMESTAMP",
            "min": "2019-12-09 13:00:00+00",
            "max": "2021-07-23 02:00:00+00",
            "avg": None,
            "unique_count": 3775,
            "null_percentage": 0.0,
            "stddev": None,
            "is_fv_feature": False,
            "is_fv_entity": False,
            "is_fv_event_timestamp": True,
        },
        {
            "column_name": "value_avg",
            "column_type": "FLOAT",
            "min": "1",
            "max": "1742",
            "avg": "126.42742197839384",
            "unique_count": 1422,
            "null_percentage": 0.0,
            "stddev": 175.07633740644545,
            "is_fv_feature": True,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "value_sum",
            "column_type": "FLOAT",
            "min": "1",
            "max": "132968",
            "avg": "663.75700483091839",
            "unique_count": 1130,
            "null_percentage": 0.0,
            "stddev": 3996.362789365462,
            "is_fv_feature": True,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "value_count",
            "column_type": "FLOAT",
            "min": "1",
            "max": "1374",
            "avg": "4.5374396135265735",
            "unique_count": 70,
            "null_percentage": 0.0,
            "stddev": 36.39923587492331,
            "is_fv_feature": True,
            "is_fv_entity": False,
            "is_fv_event_timestamp": False,
        },
        {
            "column_name": "source_name",
            "column_type": "VARCHAR",
            "min": "Diogo iPhone",
            "max": "iPhone",
            "avg": None,
            "unique_count": 3,
            "null_percentage": 0.0,
            "stddev": None,
            "is_fv_feature": False,
            "is_fv_entity": True,
            "is_fv_event_timestamp": False,
        },
    ]


def test_summarize_feature_view_model(step_count_by_source_model_summary):
    summary = summarize(StepCountBySource).to_dict(orient="records")
    assert summary == step_count_by_source_model_summary


def test_summarize_array_column():
    col_summary = summarize_column(ArrayRepeatedFields, ArrayRepeatedFields.int_arr)
    assert col_summary.empty
