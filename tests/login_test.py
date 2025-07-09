from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_test import BaseTest
from time import sleep
from pages.login_page import LoginPage
import allure
import pytest

@pytest.mark.ui
class Testlogin(BaseTest):
    @allure.story("Login Test")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self, config):
        login_data = config["login_data"]
        self.driver.get(login_data["url"])
        login_page = LoginPage(self.driver)
        login_page.login(login_data["username"], login_data["password"])
