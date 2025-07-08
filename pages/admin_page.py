from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class AdminPage:
    def __init__(self, driver):
        self.driver = driver 
        self.admin_btn = (By.XPATH, "//a[@class='oxd-main-menu-item active']")
        self.title = (By.CSS_SELECTOR, ".oxd-topbar-header-title")

    # def login_to_admin(self, username: str, password: str):
    #     self.login_page.login(username, password)

    # def is_admin_displayed(self):
    #     try:
    #        sleep(5)
    #        element = WebDriverWait(self.driver, 10).until(
    #            EC.visibility_of_element_located(*self.admin_btn))
    #        return True 
    #     except:
    #         return False

    def is_admin_clickable(self):
        try:
            sleep(5)
            admin = self.driver.find_element(*self.admin_btn)
            return admin.is_enabled()
        except:
            return False
        
    def is_title_displayed(self):
        try:
            return self.driver.find_element(*self.title).is_displayed()
        except:
            return False
    


    