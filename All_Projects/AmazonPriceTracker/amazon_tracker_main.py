from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

product_url = 'https://www.amazon.in/Boat-Rockerz-550-Headphone-Aesthetics/dp/B0856HY85J/ref=sr_1_1_sspa?crid=37J3TT3UD' \
              'FPEK&keywords=boat+headphones&qid=1646896486&sprefix=boat+hea%2Caps%2C307&sr=8-1-spons&psc=1&spLa=ZW5jcn' \
              'lwdGVkUXVhbGlmaWVyPUExTDhBN0RXVFgwTjlaJmVuY3J5cHRlZElkPUEwMTgzMjM2MkI1STFSMVRBVzE4QSZlbmNyeXB0ZWRBZElkPU' \
              'EwMDcyNTIyMlBVR1U0NUREQUhGTyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXR' \
              'ydWU='

headers = {
    "User-Agent": "en-US,en;q=0.9",
    "Accept-Language": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                       "Chrome/99.0.4844.51 Safari/537.36"

}

response = requests.get(url=product_url, headers=headers)
data = response.text

soup = BeautifulSoup(data, "lxml")

title = soup.find(name="span", id="productTitle")
main_title = (title.getText().split(" ")[8:19])

my_text = " ".join(main_title)


extracted_price = soup.find(name="span", class_="a-offscreen")
actual_price = int(extracted_price.getText().split(".")[0][1::].replace(",", ""))

my_email = "mr5527579@gmail.com"
password = "Haunted97"

if actual_price <= 1999:
    message = f"{my_text} is now {actual_price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as new_connection:
        new_connection.starttls()
        new_connection.login(user=my_email, password=password)
        new_connection.sendmail(from_addr=my_email, to_addrs="deveshk237@gmail.com",
                                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_url}")
