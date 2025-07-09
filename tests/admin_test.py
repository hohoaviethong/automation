from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.admin_page import AdminPage
@pytest.mark.ui
@pytest.mark.skip
class TestAdmin(BaseTest):  
    def test_admin_page(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        admin_page = AdminPage(self.driver)

        self.driver.implicitly_wait(15)
      
        # assert admin_page.is_admin_displayed()
        assert admin_page.is_admin_clickable()
        assert admin_page.is_title_displayed()