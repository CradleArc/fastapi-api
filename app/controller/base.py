import datetime

from fastapi import APIRouter
from starlette.responses import Response

from app.config.fastapi import FastapiConfig

base_router = APIRouter()


@base_router.get('/')
async def get_root():
    """
    访问根路径
    """
    return {
        'title': FastapiConfig.title,
        'description': FastapiConfig.description,
        'version': FastapiConfig.version,
        'time': datetime.datetime.now()
    }


@base_router.get('/robots.txt')
async def get_robots():
    """
    获取爬虫权限
    """
    return Response(content='User-agent: * \nDisallow: /', media_type='text/plain')


@base_router.get('/sys_info')
async def get_sys_info():
    """
    获取系统基本信息
    """
    from ..service.sys_info import SysInfoService

    return SysInfoService().get_sys_info()
