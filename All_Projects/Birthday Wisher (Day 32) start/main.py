import smtplib
import datetime as dt
import random

my_email = "mr5527579@gmail.com"
password = "Haunted97"

time = dt.datetime.now()
year = time.year
month = time.month
day_of_week = time.weekday()

# to crate you datetime
date_of_birth = dt.datetime(year=2003, month=6, day=11, hour=5, minute=45, second=36)
print(date_of_birth)

with open("quotes.txt") as motivate:
    lines = motivate.readlines()

random_quote = random.choice(lines)
if day_of_week == 4:
    with smtplib.SMTP("smtp.gmail.com", port=587) as new_connection:
        new_connection.starttls()
        new_connection.login(user=my_email, password=password)
        new_connection.sendmail(from_addr=my_email, to_addrs="deveshk237@gmail.com", msg=random_quote)







