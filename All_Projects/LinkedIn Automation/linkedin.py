from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

web_driver_location = Service("C:\DEVESH\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=web_driver_location, options=op)

driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")

email = driver.find_element(By.ID, "username")
email.send_keys("deveshk237@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("haunted97")

button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
button.click()
time.sleep(3)
jobs_button = driver.find_element(By.XPATH, '//*[@id="ember20"]')
jobs_button.click()

driver.maximize_window()

apply = driver.find_element(By.CSS_SELECTOR, "#ember980 a")
print(apply)


