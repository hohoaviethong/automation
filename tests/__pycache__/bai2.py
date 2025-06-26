import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        self.driver.quit()