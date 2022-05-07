# name = input("What is your name?  ").title()
# if name == "Bond":
#     print(f"Welcome on board 007")
# else:
#     print(f"Good Morning {name}")
#
# num = int(input("enter any number you want  "))
# def evens():
#     if num % 2 == 0:
#         print("the number is even")
#     else:
#         print("Odd")
#
# evens()

def the_decimal(num):
    if num - int(num) != 0:
        print(num - int(num))
    else:
         print("INTEGER")
the_decimal(99.79)

treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "Canada": 36388, "Bulgaria": 24987, "France": 24436, "Greece": 24323, "United States": 23513, "Turkey": 11126, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}

def moretrees():
    countries_list = []
    for trees in treepersqkm:
        if treepersqkm[trees] > 20000:
            countries_list.append(trees)
    print(countries_list)

moretrees()

str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"

def count_l(a=str):
    c = 0
    for i in str.split():
       if "a" in i.lower():
            print(i)
       c +=1


count_l(str)

# num = int(input("Enter the number? "))
# remainder = num // 3
# if remainder % 3 == 0:
#     print(f"{num} is divisible by 3")
# else:
#     print("It is not divisible")
#
# cost_price = int(input("Enter the cost price of the bike?   "))
# if cost_price > 100000:
#     tax = (100000 * 15) / 100
#     print(f"the tax is {tax}")
# elif 100000 >= cost_price > 50000:
#     tax = (cost_price * 10) / 100
#     print(f"the tax is {tax}")
# else:
#     tax = (cost_price * 5) / 100
#     print(f"the tax is {tax}")
#
# weekdays = ["sunday", "monday", "Tuesday", "Wednesday", "Thursday", "Friday", "saturday"]
# num = int(input("Enter the number between 1 and 7 ? "))
# if num in range(1, 8):
#     print(weekdays[num - 1])
# else:
#     print("You entered the wrong number")


#
# num = int(input("Enter the number? "))
# if num % 3 == 0 and num % 2 == 0:
#     print(f"{num} is divisible by both 2 and 3")
# else:
#     print("not divisible")
#
# character = input("Enter the character you want  ").lower()
# if character == "a" or "e" or "i" or "o" or "u":
#     print(f"{character} is a vowel")
# else:
#     print("it is a consonant")


# age1 = input("Enter the age of first person  ")
# age2 = input("Enter the age of second person  ")
# age3 = input("Enter the age of third person  ")
# age4 = input("Enter the age of fourth person  ")
#
# ages_list = []
# ages_list.append(age1)
# ages_list.append(age2)
# ages_list.append(age3)
# ages_list.append(age4)
#
# print(max(ages_list))
#
# total_no_of_working_days = int(input("enter the total number of working days  "))
# days_you_were_absent = int(input("Enter the days you were absent  "))
#
# percentage = (days_you_were_absent / total_no_of_working_days) * 100
# if percentage < 75:
#     print("You are not able to sit in exam")
# else:
#     print("You can attend the exam")

# num1 = int(input("Enter the first number  "))
# num2 = int(input("Enter the second number  "))
# num3 = int(input("Enter the third number  "))
#
# if num1 > num2 and num1 < num3 or num1 > num3 and num1 < num2:
#     print(f"{num1}")
# elif num2 > num1 and num2 < num3 or num2 > num3 and num2 < num1:
#     print(f"{num2}")
# elif num3 > num1 and num3 < num2 or num3 > num2 and num3 < num1:
#     print(f"{num3}")

# num1 = int(input("Enter the first number  "))
# num2 = int(input("Enter the second number  "))
# num3 = int(input("Enter the third number  "))
#
# if num1 + num2 > num3 and num2 + num3 > num1 and num3 + num1 > num2:
#     print("The triangle is possible")
# else:
#     print("The triangle is not possible")

# for i in range(1, 11):
#     print(f"{i} and {i*i}")
#
# total = 0
# for i in range(0, 301, 10):
#     print(i)
#
# for i in range(105, 6, -7):
#     print(i)
# for i in range(10, 0, -1):
#     print(i)
#
# num = int(input("enter the number you want the table for  "))
# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}

# should_continue = True
# num = int(input("enter the digit  "))
# p = 0
# r = num % 10
# num = num // 10
# while should_continue:
#     add = r + num
#     should_continue = False
# print(add)

# for i in "pyhton":
#     print(i, end = "  ")
#
# x = 3
# while x < 11:
#     print(x**2)
#     x += 2


# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()
#
# num = (input("enter all the numbers you want the average for  ")).split(' ')
# numbers_list =[]
# for i in num:
#     numbers_list.append(i)
# length = len(numbers_list)
#
# total = 0
# for i in numbers_list:
#     total += int(i)
# add = total
#
# average = total  / int(length)
# print(average)
#
# for i in range(5, 1, -1):
#     for j in range(i):
#         print("*", end = "  ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(i, end = " ")
#     print()
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# for i in range(1, 5, 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
#
# num = int(input("Enter the number you want to check  "))
# total = 0
# number_list = []
# for i in range(1, num):
#     if i != num:
#         remainder = num % i
#     if remainder == 0:
#         number_list.append(i)
# if sum(number_list) == num:
#     print("It is a perfect number")
# else:
#     print("not perfect")

for i in range(1, 5, 1):
    for j in range(i, i +1):
        print("A", end = " ")

    print()






