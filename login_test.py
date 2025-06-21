from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
sleep(5)
# driver.find_element(By.NAME,'username').click()
#driver.find_element(By.NAME,'username').send_keys('Admin')
#driver.find_element(By.NAME,'password').send_keys('admin123')
#driver.find_element(By.XPATH,'//button[@type="submit"]').click() 
#assert driver.find_element(By.XPATH,'//H6[text()="dashboard"]').text=='Dashboard'
print(driver.title)''
driver.get("https://google.com/")
print(driver.title)
driver. back()
print(driver.title)

