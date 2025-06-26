import pytest
from selenium import webdriver
from utils.read_config import ConfigReader
class BaseTest:
    @pytest.fixture(autouse=True)

    def setup_class(self):
        # Setup: Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get(ConfigReader.get_url())
        self.driver.maximize_window()
        yield self.driver  # This will be used in the test methods
        # Teardown: Quit the WebDriver
        self.driver.quit()
   

