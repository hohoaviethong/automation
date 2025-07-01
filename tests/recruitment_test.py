from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.recruitment_page import RecruitmentPage

class TestRecruitPage(BaseTest):
    def test_recruit_page(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.click_recruitment
        recruitment_page.click_vacancies
        recruitment_page.click_add