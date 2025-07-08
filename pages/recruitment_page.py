from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support import expected_conditions as EC
from utils.read_config import ConfigReader
from time import sleep


class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver 
        self.recruit_btn = (By.XPATH, "//span[text()='Recruitment']")
        self.vacancies_btn = (By.XPATH, "//a[text()='Vacancies']")
        self.add_btn = (By.XPATH, "//button[normalize-space()='Add']")
        self.add_vacancy_page = (By.XPATH, "//h6[text() = 'Add Vacancy']")
        self.save_btn = (By.XPATH, "//button[@type='submit']")
        self.edit_vacancy_page = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']")
        self.cancel_btn = (By.XPATH, "//button[text()=' Cancel ']")
        self.vacancy_page = (By.XPATH, "//h5[@class='oxd-text oxd-text--h5 oxd-table-filter-title']")
        self.checkbox_active = (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
        self.checkbox_publish = (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]")
    

    #1.Click on Recruitment button
    def click_recruitment(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.recruit_btn))
        element.click()

       
    #2.Click on Vacancies button  
    def click_vacancies(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.vacancies_btn))
        element.click()


    #3.Click on Add button
    def click_add_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_btn))
        element.click()


    #4. Verify the Add Vacancy page displays    
    def is_Add_Vacancy_displayed(self):
        try:
           element = WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located(self.add_vacancy_page))
           return True 
        except:
            return False
         

    #5. Fill in the Add Vacancy form
        #vacancy name
    def vacancy_name_input(self, vacancy_data):  
        vacancy_name_input = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Vacancy Name']/following::input[1]"))
    )
        vacancy_name_input.send_keys(vacancy_data["Vacancy Name"])

       #job title
    def select_job_title(self):
        job_title_dropdown = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
        )
        job_title_dropdown.click()
         # select the job title from the dropdown
        self.job_title = ConfigReader.get_vacancy_raw()["Job Title"]
        select_job_title = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(By.XPATH, f"//div[@class = 'oxd-select-text-input']")
        )
        select_job_title.click()
       
        #Description 
    def description_input(self, vacancy_data):
        description_input = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Type description here']"))
    )
        description_input.send_keys(vacancy_data["Description"])

        # hiring manager
    def hiring_manager_input(self, vacancy_data):
        hiring_manager_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
        )
        hiring_manager_input.send_keys(vacancy_data["Hiring Manager"])
        sleep(5)  # Wait for the dropdown to populate
        hiring_manager_input.send_keys(Keys.ARROW_DOWN)  # Select the hiring manager from the dropdown
        hiring_manager_input.send_keys(Keys.ENTER)  # Select the hiring manager from the dropdown

        # number of positions
    def number_of_positions_input(self): 
        action = ActionChains(self.driver)
        number_of_positions = self.driver.find_element(By.XPATH, "//label[text()='Number of Positions']/following::input[1]")
        action.click(number_of_positions)
        action.send_keys('1').perform()  
       
        # checkbox1
    def set_checkbox1(self, should_be_checked: bool):
        checkbox1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkbox_active))
        is_checked = checkbox1.is_selected()

        if is_checked != should_be_checked:
            sleep(3)
            checkbox1.click()

        #checkbox2
    def set_checkbox2(self, should_be_checked: bool):
        checkbox2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkbox_publish))
        is_checked = checkbox2.is_selected()

        if is_checked != should_be_checked:
            sleep(3)
            checkbox2.click()


    #6.Click the Save button
    def click_save_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_btn))
        element.click()

   
    #7. Verify the Edit Vacancy page displays
    def is_edit_vacancy_page_displayed(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.edit_vacancy_page)
            )
            return True
        except:
            return False
        

    #8. Click on Cancel button
    def click_cancel_btn(self):
        cancel_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cancel_btn)
        )
        cancel_btn.click()
    
       
    # 9.Verify the Vacancies page dispatch again
    def is_vacancies_page_displayed(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.vacancy_page)
            )
            return True
        except:
            return False
        
        
    #10. Click on search button:
    # def click_search_btn(self):
        #(//input[@type='checkbox'])[1]