from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

web_driver_location = Service("C:\DEVESH\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=web_driver_location, options=op)

driver.execute_cdp_cmd(
    "Browser.grantPermissions",
    {
        "origin": "https://tinder.com",
        "permissions": ["geolocation"]
    },
)

driver.maximize_window()
driver.get("https://tinder.com/")

time.sleep(2)
log_in = driver.find_element(By.XPATH, '//*[@id="t-2073920312"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div'
                                       '/div[2]/div[2]/a')
log_in.click()

cookie = driver.find_element(By.XPATH, '//*[@id="t-2073920312"]/div/div[2]/div/div/div[1]/div[1]/button/span')
cookie.click()

# time.sleep(2)
# more_options = driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div[1]/div/div[3]/span/button')
# more_options.click()

time.sleep(2)
with_facebook = driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div[1]/div/div[3]/span/div[2]/button')
with_facebook.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.ID, "email")
email.send_keys("8076431825")

password = driver.find_element(By.ID, "pass")
password.send_keys("haunted97")

log_in_fb = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
log_in_fb.click()

driver.switch_to.window(base_window)
print(driver.title)

# time.sleep(5)
# allow = driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div/div/div[3]/button[1]')
# allow.click()
#
#
# enable = driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div/div/div[3]/button[1]')
# enable.click()

for n in range(100):

    # Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
                                          '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/di'
                                          'v[2]/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
