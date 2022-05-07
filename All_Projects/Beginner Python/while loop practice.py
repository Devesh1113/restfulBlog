# practice exercises
def num(n):
    new_n = str(n)
    return int(new_n) + int((new_n + new_n)) + int((new_n + new_n + new_n))


print(num(5))

print(help(abs))

def check_num(n):
    if n in range(100, 1000):
        print(n)

string = "a boy"
if "is" in string:
    print(string)
else:
    print(f"is {string}")

import multiprocessing
print(multiprocessing.cpu_count())

first = "devesh"
second = "nothing"
if first != second:
    third = first
    first = second
    print(first)
    print(third)

list = []
numbers = input("Enter the numbers using commas").split()


def check():
    for i in numbers:
        for j in numbers:
            if i == j:
                return True
            else:
                return False

print(check())


