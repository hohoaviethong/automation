import pytest
from tests.base_test import BaseTest
import requests  

class MyInfoAPI:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def get_personal_details(self):
        url = f"{self.base_url}/web/index.php/api/v2/pim/employees/7/personal-details"
        return self.session.get(url)

    def get_employee_list(self, limit=10, offset=0):
        url = f"{self.base_url}/web/index.php/api/v2/pim/employees"
        payload = {"limit": limit, "offset": offset}
        return self.session.post(url, json=payload)