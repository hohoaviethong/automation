# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait   
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import pytest

# class LoginPage():
#     def __init__(self, driver):
#         self.timeout = 10
#         self.driver = driver
#         self.username_field = (By.XPATH, "//input[@name='username']")
#         self.password_field = (By.XPATH, "//input[@name='password']")
#         self.login_button = (By.XPATH, '//button[@type="submit"]')

#     def enter_username(self, username: str):
#     username_input = WebDriverWait(self.driver, self.timeout).until(
#         lambda d: d.find_element(*self.username_field)
#     )
#     username_input.send_keys(username)

#     def enter_password(self, password:str):
#     password_input = WebDriverWait(self.driver, self.timeout).until(
#         lambda d: d.find_element(*self.password_input)
#     )
#     password_input.send_keys(password)

#     def click_login_button(self):
#     login_button = WebDriverWait(self.driver, self.timeout).until(
#         lambda d: d.find_element(*self.login_button)
#     )
#     login_button.click()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

class LoginPage():
    def __init__(self, driver):
        self.timeout = 10
        self.driver = driver
        self.username_field = (By.XPATH, "//input[@name='username']")
        self.password_field = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, '//button[@type="submit"]')

    def enter_username(self, username: str):
        username_input = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.username_field)
        )
        username_input.send_keys(username)

    def enter_password(self, password: str):
        password_input = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.password_field)
        )
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*self.login_button)
        )
        login_button.click()