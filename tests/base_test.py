import pytest
from selenium import webdriver
from utils.read_config import ConfigReader
import allure
import requests



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
        # This hook is used to capture the outcome of the test
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_call", rep)
class BaseTest:       
    @pytest.fixture(autouse=True)

    # def setup_class(self, request):
    #     # Setup: Initialize the WebDriver
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(ConfigReader.get_url())
    #     self.driver.maximize_window()

    #     # API setup:
    #     session = requests.Session()
    #     request.cls.session = session

    #     yield self.driver  # This will be used in the test methods
    #     # Teardown: Quit the WebDriver
    #     if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
    #         allure.attach(
    #             self.driver.get_screenshot_as_png(),
    #             name=f"failure_{request.node.name}",
    #             attachment_type=allure.attachment_type.PNG
    #         )
      
    #     self.driver.quit()

    def setup(self, request):
        self.driver = None
        self.session = None

        base_url = ConfigReader.get_url()

        if "ui" in request.keywords:
            # Setup cho UI test
            self.driver = webdriver.Chrome()
            self.driver.get(ConfigReader.get_url())
            self.driver.maximize_window()

        if "api" in request.keywords:
            # Setup cho API test
            self.session = requests.Session()

        request.cls.driver = self.driver
        request.cls.session = self.session
        request.cls.base_url = base_url 

        yield

        # Teardown
        if self.driver:
            if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name=f"failure_{request.node.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            self.driver.quit()

        if self.session:
            self.session.close()
