from datetime import datetime

from app.schema.base import InfoSchema, RespDetailSchema


class TestInfoSchema(InfoSchema):
    parent_name: str


class TestDetailSchema(TestInfoSchema):
    created_time: datetime
    updated_time: datetime


class TestRespDetailSchema(RespDetailSchema):
    detail: TestDetailSchema = None
