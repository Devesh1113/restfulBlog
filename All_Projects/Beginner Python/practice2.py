#age = input("what's your age?  ")
#name = input("What's your name?  ")
#print(float(age))
#combined = str(age) + str(name)
#print(combined)
#print(name[1])

import random
list_of_cricketers_india = ["virat kohli", "ms dhoni", "yuvraj" , "bumrah" , "pandya", "kedhar jadhav", "rohit sharma", "rishabh" ]
print(random.choice(list_of_cricketers_india))






num =8 / 3
print(round(num, 2))
num += 67
print(num)
print(f"this is a decimal number {num}")
import random
num = random.random() * 477
print(num)
list_of_cricketers_india = ["virat kohli", "ms dhoni", "yuvraj" , "bumrah" , "pandya", "kedhar jadhav", "rohit sharma", "rishabh" ]
list_of_cricketers_austrailia = ["smith","warner", "pat cummins", "starc", "tim payne", "hazlewood", "khwaja", "lyon",]
list_of_cricketers = [list_of_cricketers_india, list_of_cricketers_austrailia]

num1 = len(list_of_cricketers_india)
print(num1)
name1 = random.randint(0, num1 - 1)
print(name1)
listed_cricketer = list_of_cricketers_india[name1]
print(listed_cricketer)






