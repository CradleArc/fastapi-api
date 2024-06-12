from fastapi import APIRouter

from . import category
from . import org
from . import user
from . import demo

api_v1_router = APIRouter()
api_v1_router.include_router(category.router, prefix="/category", tags=["category"])
api_v1_router.include_router(org.router, prefix="/org", tags=["org"])
api_v1_router.include_router(user.router, prefix="/user", tags=["user"])
api_v1_router.include_router(demo.router, prefix="/demo", tags=["demo"])
