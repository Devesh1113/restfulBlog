#Coding Exercise


two_digit_number = str(input("enter your two digit number"))
print(type(two_digit_number))
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Day 2 Project - Tip Calculator

print("Welcome to the Tip Calculator")
bill = float(input("what is your total bill?  $"))

per1 = 10
per2 = 12
per3 = 15
percent = int(input(f"What percentage tip you would like to give? $ {per1}, {per2} or {per3}"))

people = int(input("How many will split the Bill?  "))


num = (float(bill) * float(percent))
tip = float(num / 100)
print("Every person has to pay a tip of  " + "$" + str(round(tip, 2)))
total_amount_to_be_paid = float(tip) + float(bill)
print("total amount to be paid is  " + "$" + str(round(total_amount_to_be_paid, 2)))

# Leap Year Excerise
year = int(input("Enter the year you want to check :  "))

if year % 4 == 0:
   if year % 100 == 0:
      if year % 400 == 0:
          print("it is a leap year")
      else:
          print("its not a leap year")

   else:
       print("It is a leap year")
else:
    print("Its not a leap year")












