#importing drivers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys, ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time



# RECORRECT THIS CODE AS THEIR MAY BE CHANGE IN THE SCRIPT OF WEBSITE

SERVICE = Service(executable_path='/home/suraj/Desktop/python/Selenium/chromedriver.exe')
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = "OUR INSTAGRAM USERNAME"
PASSWORD = "YOUR INSTAGRAM PASSWORD"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(service=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_element(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(SERVICE)
bot.login()
bot.find_followers()
bot.follow()