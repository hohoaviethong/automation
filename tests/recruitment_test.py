from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.recruitment_page import RecruitmentPage
from utils.read_config import ConfigReader


@pytest.fixture
def vacancy_data():
    return ConfigReader.process_vacancy_data()
@pytest.mark.ui
class TestRecruitPage(BaseTest):
    def test_recruit_page(self, vacancy_data):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.click_recruitment()
        recruitment_page.click_vacancies()
        recruitment_page.click_add_btn()
        assert recruitment_page.is_Add_Vacancy_displayed()
        vacancy_data = ConfigReader.process_vacancy_data()
        recruitment_page.vacancy_name_input(vacancy_data)
        recruitment_page.select_job_title()
        recruitment_page.description_input(vacancy_data)
        recruitment_page.hiring_manager_input(vacancy_data)
        recruitment_page.number_of_positions_input()
        recruitment_page.set_checkbox1(vacancy_data["Active"])
        recruitment_page.set_checkbox2(vacancy_data['Publish in RSS Feb and Web Page'])
        recruitment_page.click_save_btn()
        assert recruitment_page.is_edit_vacancy_page_displayed()
        recruitment_page.click_cancel_btn()
        assert recruitment_page.is_vacancies_page_displayed()

    
    
    
    # add_page = AddVacancyPage(driver)
    # add_page.fill_add_form(vacancy_data)  