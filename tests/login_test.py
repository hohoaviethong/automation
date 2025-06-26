from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_test import BaseTest
from time import sleep
from pages.login_page import LoginPage
class Testlogin(BaseTest):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()

