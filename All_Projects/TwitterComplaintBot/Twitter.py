from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = Service("C:\DEVESH\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()

TWITTER_EMAIL = "mr5527579@gmail.com"
TWITTER_PASSWORD = "!PI9u71(%XXltsYg4"


class InternetSpeedTwitterBot:
    def __int__(self):
        self.up = 0
        self.down = 0

    def get_internet_speeds(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH, options=op)
        self.driver.maximize_window()
        self.driver.get('https://www.speedtest.net/')
        time.sleep(3)
        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(60)

        self.upload_speed = self.driver.find_element(By.XPATH,
                                                     '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                     'div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div['
                                                     '2]/span').text
        print(self.upload_speed)
        self.download_speed = self.driver.find_element(By.XPATH,
                                                       '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div'
                                                       '[3]/div[3]'
                                                       '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.download_speed)

    def tweet_at_provider(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH, options=op)
        self.driver.maximize_window()
        self.driver.get('https://twitter.com/')
        time.sleep(2)
        self.sign_in = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/'
                                                'div[3]/div[5]/a')
        self.sign_in.click()
        time.sleep(3)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/'
                                                   'div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)

        time.sleep(2)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div'
                                                         '/div/div[2]/div[2]/div[1]/div/div/div[6]')
        next_button.click()

        time.sleep(1)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div'
                                                      '/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/d'
                                                      'iv[1]/input')
        password.send_keys(TWITTER_PASSWORD)

        time.sleep(2)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/di'
                                                    'v/div[2]/div[2]/div[2]/div/div[1]')
        log_in.click()

        # message = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/di'
        #                                              'v[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/'
        #                                              'div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        # message.send_keys(f"Hey Internet Provider, Why is my internet speed {self.download_speed} down/{self.upload_speed} "
        #                   f"up When i pay for 150 down/10 up")

        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/di'
                                                   'v/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div['
                                                   '2]/div')
        tweet.click()

bot = InternetSpeedTwitterBot()
# bot.get_internet_speeds()
bot.tweet_at_provider()
