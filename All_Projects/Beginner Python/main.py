import random

random_num = random.randint(1,5)
print(random_num)

random_decimal_num = random.random()
print(random_decimal_num)
#if we want to increase the range of 0 to any number we want we can do. let's say a number to 8
random_decimal2 = random.random() * 67
print(random_decimal2)

#head or tail exercise

random_num2 = random.randint(0, 1)

if random_num2 == 1:
    print("Heads")
else:
    print("Tails")
