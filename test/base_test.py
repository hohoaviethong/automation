import pytest
from selenium import webdriver

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_class(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        self.driver.quit()