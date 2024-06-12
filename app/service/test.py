from app.service.base import BaseService

from ..dao.test import TestDao
from ..model.test import Test


class TestService(BaseService):
    def __init__(self, auth_data: dict = {}):
        user_id = auth_data.get('user_id', 0)
        self.Model = Test
        self.dao = TestDao(user_id)
        self.dao.Model = Test

        super().__init__(user_id, auth_data)
