##################### Hard Starting Project #####################
import pandas
import pandas as pd
import datetime as dt
import random
time = dt.datetime.now()

day = time.day
month = time.month
print(day)

today_tuple = (day, month)

df = pandas.read_csv("birthdays.csv")
myvar2 = pd.DataFrame(df)


with open("letter_templates/letter_1.txt") as l1:
    x1 = l1.read()
    letter1 = l1.readlines()

with open("letter_templates/letter_2.txt") as l2:
    x2 = l2.read()
    letter2 = l2.readlines()

with open("letter_templates/letter_3.txt") as l3:
    x3 = l3.read()
    letter3 = l3.readlines()

my_list = [letter1, letter2, letter3]
random_letter = random.choice(my_list)
birthday_dict = {(row.day, row.month): row for (index, row) in myvar2.iterrows()}

if today_tuple in birthday_dict:
    for name in random_letter:
        new_name = name.strip()















