from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(5)
# get element username and send user account
user_name = driver.find_element(By.NAME, "username")
user_name.send_keys("Admin")
# get pass element and send password
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")
# click on login button
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(5)

# verify that user is on Dashboard page
dashboard_text = driver.find_element(By.XPATH,"//h6[text()='Dashboard']")
assert dashboard_text.text == "Dashboard"