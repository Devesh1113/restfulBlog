

number = str(98764)
# num1 = 0
# for num in number:
#     num1 += int(num)
# print(num1)

for i in range(0, 4):
    print(" " * 0 + "*" * 5)
    if i == 3:
        print(" " * 4 + "*" * 5)

for i in range(1, 5):
    for j in range(1, 1 + i):
        print(j, end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 1 + i):
        print(i, end=" ")
    print()

# num = 1
# for i in range(1):
#     for j in range(1, 11):
#         for z in range(j, j + num):
#             num += 1
#             print(z, end=" ")
#         print()

string = "Hi my Name IS DEVesh"

x = 0
y = 0
for case in string:
    for case2 in case:
        if case2 == " ":
            pass
        elif case2 == case2.upper():
            x += 1
        elif case2 == case2.lower():
            y += 1

print(x)
print(y)












