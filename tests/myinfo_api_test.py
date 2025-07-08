import pytest
from api.myinfo_api import MyInfoAPI
from tests.base_test import BaseTest
import allure
import requests


@pytest.mark.usefixtures("setup")
@pytest.mark.api
class TestMyInfo:
    def test_get_personal_details(self):
        api = MyInfoAPI(self.session, self.base_url)
        res = api.get_personal_details()
        assert res.status_code == 200