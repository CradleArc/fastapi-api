from fastapi import APIRouter, Depends
from app.schema.base import ListArgsSchema, RespBaseSchema, RespIdSchema, RespListSchema
from app.utils.auth import get_auth_data
from app.utils.custom_route import CustomRoute

from ..schema.test import TestInfoSchema, TestRespDetailSchema
from ..service.test import TestService

router = APIRouter(route_class=CustomRoute)


@router.post('/list', response_model=RespListSchema)
async def list(*, args: ListArgsSchema, auth_data: dict = Depends(get_auth_data)):
    args.user_id = auth_data.get('user_id')
    return TestService(auth_data).list(args)


@router.get('/{id}', response_model=TestRespDetailSchema)
async def read(id: int, auth_data: dict = Depends(get_auth_data)):
    resp = TestRespDetailSchema()
    resp.detail = TestService(auth_data).read(id)
    return resp


@router.post('', response_model=RespIdSchema, response_model_exclude_none=True)
async def create(*, info: TestInfoSchema, auth_data: dict = Depends(get_auth_data)):
    return TestService(auth_data).create(info)


@router.put('/{id}', response_model=RespBaseSchema)
async def update(*, info: TestInfoSchema, auth_data: dict = Depends(get_auth_data)):
    return TestService(auth_data).update(info)


@router.delete('/{id}', response_model=RespBaseSchema)
async def delete(id: int, auth_data: dict = Depends(get_auth_data)):
    return TestService(auth_data).delete(id)
