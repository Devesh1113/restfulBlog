import random
print("Welcome to the PAN CARD NUMBER GENERATOR!")
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password1 = ""
for letter1 in range(1, 6):
    random1 = random.choice(letters)
    password1 += random1


password2 = ""
for letter2 in range(1, 5):
    random2 = random.choice(numbers)
    password2 += random2


password3 = ""
for letter3 in range(1, 2):
    random3 = random.choice(letters)
    password3 += random3


print(f"{password1}{password2}{password3}")

















numbers = [1, 2, 3, 4, 59, 7, 9, 12, 45]
sum = 0
for num in numbers:
    num >= sum
    sum = num
print(f"the sum of all numbers is {sum} ")

total = 0
for number in range(1, 101,):
    total = total + number
print(total)








#Password Generator
import random
print("Welcome to the PyPassword Generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = input("how many letters you want to input in your password  ")
nr_numbers = input("how many number you want to put in your password ")
nr_symbols = input("how many symbols you want to put in your password  ")

password = ""
for letter in range(1, int(nr_letters) + 1):
    random_letters = random.choice(letters)
    password += random_letters


num_pass = ""
for number in range(1, int(nr_numbers) + 1):
    random_numbers = random.choice(numbers)
    num_pass += random_numbers


symbol_pass = ""
for symbol in range(1, int(nr_symbols) + 1):
    random_symbols = random.choice(symbols)
    symbol_pass  += random_symbols

print(f"here is your password:  {password}{num_pass}{symbol_pass} ")


























