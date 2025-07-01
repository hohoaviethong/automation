from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support import expected_conditions as EC

class RecruitmentPage:
     def __init__(self, driver):
        self.driver = driver 
        self.recruit_btn = (By.XPATH, '//span[text()="Recruitment"]')
        self.vacancies_btn = (By.XPATH, '//span[text()="Vacancies"]')
        self.add_btn = (By.XPATH, '//button[normalize-space()="Add"]')

     def click_recruitment(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(*self.recruit_btn))
        element.click()
       
        
     def click_vacancies(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(*self.vacancies_btn))
        element.click()

     def click_add(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(*self.add_btn))
        element.click()
          
 
     
           
   
   
