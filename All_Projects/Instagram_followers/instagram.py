from telnetlib import EC
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

CHROME_DRIVER_PATH = Service("C:\DEVESH\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
INSTA_PASS = "&nc72!TSxmd#2W5e"
INSTA_USERNAME = "python._.i.s_.fun"
USERNAME = 'nancyjewel_mcdonie_'


class InstaFollower:
    def __int__(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH, options=op)

    def log_in(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH, options=op)
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)
        username = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/f'
                                                      'orm/div/div[1]/div/label/input')
        username.send_keys(INSTA_USERNAME)

        time.sleep(2)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASS)

        time.sleep(2)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()

        time.sleep(5)
        log_info = self.driver.find_element(By.CSS_SELECTOR, ".cmbtv button")
        log_info.click()

        time.sleep(1)
        not_now = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_now.click()

    def find_followers(self):
        time.sleep(4)
        search = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(USERNAME)

        time.sleep(2)
        person = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3'
                                                    ']/div/div[2]/div/div[1]/a')
        person.click()

        time.sleep(3)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/l'
                                                       'i[2]/a')
        followers.click()

        time.sleep(3)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        time.sleep(2)
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        time.sleep(2)
        follow_list = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for follow in follow_list:
            if follow.text != "Follow":
                pass
            else:
                follow.click()
                time.sleep(2)


insta_followers = InstaFollower()
insta_followers.log_in()
insta_followers.find_followers()
insta_followers.follow()
