from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


web_driver_location = Service("C:\DEVESH\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=web_driver_location, options=op)
driver.get("https://www.amazon.in/Boat-Rockerz-550-Headphone-Aesthetic"
           "s/dp/B0856HY85J/ref=sr_1_1_sspa?crid=37J3TT3UDFPEK&keywords=boat%2Bheadphones&qid=1646896486&sprefix"
           "=boat%2Bhea%2Caps%2C307&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTDhBN0RXVFgwTjlaJmVuY3J5cHRlZElkPUEwM"
           "TgzMjM2MkI1STFSMVRBVzE4QSZlbmNyeXB0ZWRBZElkPUEwMDcyNTIyMlBVR1U0NUREQUhGTyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb24"
           "9Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1")

price = driver.find_element(By.ID, value="twotabsearchtextbox")
print(price)
print(price.tag_name)
print(price.size)
print(price.get_attribute("nav-input"))

doc_link = driver.find_element(By.CLASS_NAME, "a-size-base")
print(doc_link)

# using x path to get a html element
price_using_x_path = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/'
                                                   'tbody/tr[2]/td[2]/span[1]/span[2]')
print(price_using_x_path.text)

# finding multiple elements

driver.get("https://www.python.org/")
dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

dates_list = [date.text for date in dates]

links_text = driver.find_elements(By.CSS_SELECTOR, ".event-widget a")

links_list = [link.text for link in links_text]

events_dict = {}

for i in range(len(dates_list)):
    events_dict[i] = {
        "time": dates_list[i],
        "events": links_list[i + 1],
    }

print(events_dict)

# How to click on something using selenium

driver.get("https://en.wikipedia.org/wiki/Main_Page")
element = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# element.click()

# using find_method
all_portals = driver.find_element(By.PARTIAL_LINK_TEXT, "All portals")
# all_portals.click()

# Typing into an element
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
# Keys class used to return like Entering after typing a text using send_keys method
search.send_keys(Keys.ENTER)

# Challenge

driver.get("http://secure-retreat-92358.herokuapp.com/")

enter_name = driver.find_element(By.NAME, "fName")
enter_name.send_keys("Devesh")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Kumar")

email = driver.find_element(By.NAME, "email")
email.send_keys("deveshk237@gmail.com")

sign_up = driver.find_element(By.CLASS_NAME, "btn-block")
sign_up.send_keys(Keys.ENTER)

