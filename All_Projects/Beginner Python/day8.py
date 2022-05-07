def devesh():
    print("hello")
    print("this is Devesh!")
    print("How are you?")


devesh()


# for 1 input
def devesh2(name):
    print(f"hello {name}")
    print("this is Devesh!")
    print(f"How are you ?")


devesh2("nancy")


# for more than 1 input
def devesh2(name, name2):
    print(f"hello {name}")
    print("this is Devesh!")
    print(f"How are you {name2}?")


devesh2("nancy", "virat")

# Area Calculation
import math


def paint_calc(height, width, cover):
    num_of_cans = (test_h * test_w) / coverage
    print(f" You will need {math.ceil(num_of_cans)} cans of paint")


test_h = int(input("Height of the wall: "))
test_w = int(input("width of the wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# prime Number Checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("a prime number")
    else:
        print(" not a prime number ")


n = int(input("check this number:  "))
prime_checker(number=n)

text = input("Type anything you want you want to reverse")


def string_reverser(my_text):
    string = ""
    devesh = len(text)
    while devesh > 0:
        string += my_text[devesh - 1]
        devesh = devesh - 1
        return string


string_reverser(my_text=text)
