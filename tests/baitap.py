import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")
hide_btn = driver.find_element(By.XPATH, "//input[@id='hide-textbox']")
hide_btn.click()
sleep(5)
show_btn = driver.find_element(By.XPATH, "//input[@type='submit']")

#using Javascript
displayed_texbox = driver.find_element(By.XPATH, "//input[@name='show-hide']")
driver.execute_script("arguments[0].value = 'Hello word'", displayed_texbox)
sleep(5)
show_btn.click()
sleep(5)