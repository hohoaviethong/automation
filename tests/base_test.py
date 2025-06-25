import pytest
from selenium import webdriver

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        # Setup: Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        yield self.driver  # This will be used in the test methods
        # Teardown: Quit the WebDriver
        self.driver.quit()
   
