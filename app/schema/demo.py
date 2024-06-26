from datetime import datetime

from app.schema.base import InfoSchema, RespDetailSchema


class DemoInfoSchema(InfoSchema):
    parent_name: str


class DemoDetailSchema(DemoInfoSchema):
    created_time: datetime
    updated_time: datetime


class DemoRespDetailSchema(RespDetailSchema):
    detail: DemoDetailSchema = None
