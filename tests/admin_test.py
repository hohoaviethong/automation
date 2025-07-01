from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.admin_page import AdminPage

class TestAdmin(BaseTest):  
    def test_admin_page(self):
        admin_page = AdminPage(self.driver)
        admin_page.login_to_admin("Admin", "admin123")
        assert admin_page.is_admin_displayed(), "Admin button is not displayed"
        assert admin_page.is_admin_clickable(), "Admin button is not clickable"
        assert admin_page.is_title_displayed(), "Title is not displayed"
