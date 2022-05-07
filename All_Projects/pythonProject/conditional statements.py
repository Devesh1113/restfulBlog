# Pizza Store
print("welcome to Devesh Pizza Store")
size = input("what size Pizza do you want? s, m, l  ")
add_pepperoni = input("do you want to add pepperoni?  y or n  ")
extra_cheese = input("Do you want to add extra cheese?  y or n  ")

if size == "s":
    prize = + 15
elif size == "m":
    prize = + 20
else:
    prize = + 25
if add_pepperoni == "y":
    if size == "s":
        prize += 2
    else:
        prize += 3
if extra_cheese == "y":
    prize += 1
print(f" Your Final bill is ${prize}")
# Roller Coaster

print("Welcome to the RollerCoster")

height = input("type your height in cm  ")

if int(height) >= 150:
    print("you can ride the rollercoaster")
    age = input("Enter Your Age! ")
    if int(age) >= 18:
        print("Fare for the Ride is $20 I HOPE YOU ENJOY ")
    else:
        print("Fare for the ride is $12 HAVE A MEMORABLE RIDE")
else:
    print("Sorry you are not able to ride the Rollercoaster ")

# odd or Even Exercise

num = int(input("Type the number that you want to check! "))

remainder = (num % 2)
if remainder >= 1:
    print("The number is Odd")
else:
    print("the number is Even")
# Nested if/else with previous example
