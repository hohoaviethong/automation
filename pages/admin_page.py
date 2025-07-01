from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from pages.login_page import LoginPage

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)  
        # Gợi ý chuẩn nhất cho Bé
        admin_btn = (By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='Admin']")
        self.title = (By.CSS_SELECTOR, ".oxd-topbar-header-title")

    def login_to_admin(self, username: str, password: str):
        self.login_page.login(username, password)

    def is_admin_displayed(self):
        try:
            return self.driver.find_element(*self.admin_btn).is_displayed()
        except:
            return False

    def is_admin_clickable(self):
        try:
            admin = self.driver.find_element(*self.admin_btn)
            return admin.is_enabled() and admin.is_displayed()  
        except:
            return False
        
    def is_title_displayed(self):
        try:
            return self.driver.find_element(*self.title).is_displayed()
        except:
            return False
    


    