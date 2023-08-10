import pandas as pd
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service  = Service(executable_path='/home/suraj/Desktop/python/Selenium/chromedriver.exe')
driver =webdriver.Chrome(service = service)
driver.get('https://www.python.org/')
# event = driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]')
# print([eve.text for eve in event][0])

# another way
# easy just selectt the unique part of css 
# lik3 '.event_widget' is unique part of class than add tag which is it in
# for ids use#
eve_tme = driver.find_elements(By.CSS_SELECTOR ,'.event-widget time')
eve_date = [e.text for e in eve_tme]
events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
Events = [e.text for e in events]
driver.quit()

# export it as csv file
df = pd.DataFrame({'Date(2023)':eve_date ,'Events':Events})

df.to_csv('df',index = False) # index false make sure row index i.e 0,1,2 won't be present in file
