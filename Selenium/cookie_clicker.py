# #---------------------
#importing drivers
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys, ActionChains
service = Service(executable_path='/home/suraj/Desktop/python/Selenium/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(5)
 #clicking language
click_lang = driver.find_element(By.ID, 'langSelect-EN')
ActionChains(driver).click(click_lang).perform()
time.sleep(5)
clicker = driver.find_element(By.ID, 'bigCookie')

def cookie_clicker():
     # variables
    hands_count = 0
    grandma_count = 0
    tanks_count = 0
    cactus_count = 0
    start_time = time.time()
    while True:
        ActionChains(driver).click(clicker).perform()
        cookies = int(driver.find_element(By.ID, 'cookies').text.split(' ')[0])
        grandma = driver.find_element(By.XPATH, '//*[@id="productPrice1"]')
        hands = driver.find_element(By.XPATH, '//*[@id="productPrice0"]')
        
        if cookies > int(hands.text):
            if hands_count < 6:
                ActionChains(driver).click(hands).perform()
                hands_count += 1
            elif cookies > int(grandma.text) and grandma_count < 10:
                if (grandma_count > 4 and hands_count < 20) and int(hands.text) > cookies :
                    ActionChains(driver).click(hands).perform()
                    hands_count += 1
                elif grandma_count < 10:
                    ActionChains(driver).click(grandma).perform()
                    grandma_count += 1
                else:
                    tanks = driver.find_element(By.XPATH, '//*[@id="productPrice2"]')
                    cactus = driver.find_element(By.XPATH, '//*[@id="productPrice3"]')
            
                    x = int(tanks.text) if len(tanks.text)>0 else 0 
                    y = int(cactus.text) if len(cactus.text)>0 else 0
                    if(cookies > x and tanks_count <= 5) and x!=0:
                        ActionChains(driver).click(tanks).perform()
                        tanks_count += 1
                    elif (cookies > y and cactus_count <= 3) and y!=0:
                        ActionChains(driver).click(cactus).perform()
                        cactus_count += 1
                    else:
                        ActionChains(driver).click(grandma).perform()
                        grandma_count += 1
        elapsed_time = time.time() - start_time
        if elapsed_time > 300:
            break
cookie_clicker()
time.sleep(10)
driver.close()