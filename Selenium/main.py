from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/home/suraj/Desktop/python/Selenium/chromedriver.exe')

# We can use chromeoption as it provides various options for now go simple
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options) 

driver = webdriver.Chrome(service = service)  
driver.get('https://www.amazon.com/')

#well it closes automatically but
# we can close tabs
# driver.close()
driver.quit() #  will quit webdriver and close all associated browser windows 