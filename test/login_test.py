from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base_test import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

class Testlogin(BaseTest):
    def test_login(self):
        driver = self.driver
        driver.find_element(By.NAME, 'username').send_keys('Admin')
        driver.find_element(By.NAME, 'password').send_keys('admin123')
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        sleep(2)
        assert "OrangeHRM" in driver.title
