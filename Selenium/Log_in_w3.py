
#importing drivers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys, ActionChains
import time
service = Service(executable_path='/home/suraj/Desktop/python/Selenium/chromedriver.exe')
driver = webdriver.Chrome(service = service)
driver.get('https://www.w3schools.com/')

clickable = driver.find_element(By.ID, "w3loginbtn")

ActionChains(driver)\
.click(clickable)\
.perform()

signin = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[4]/div[1]/div/div[4]/div[2]/button[1]')
ActionChains(driver)\
.click(signin)\
.perform()


driver.quit()
# signout = driver.find_element(By.ID ,'logout-link')
# ActionChains(driver)\
# .click(signout)\
# .perform()

