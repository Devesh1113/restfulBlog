





























# treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("welcome to the treasure island\nyour mission is to find the treasure")
direction = input("where do you want to go? you have to choose between left and right ")

if direction == "left":
    choice = input('You have come to a lake. there is an island in middle of the lake. type "wait" to wait on the island or type "swim" to swim across the lake').lower()
    if choice == "wait":
       door = input("you have the found the gate. but you have to choose between three gates. which gate you want to choose? choose between red , blue , yellow").lower()
       if door == "yellow":
           print("congratulation you have found the treasure. YOU WIN")
       else:
           print(" YOU LOOSE GAME OVER!")
    else:
        print(" YOU LOOSE GAME OVER!")
else:
    print(" YOU LOOSE GAME OVER!")





























































print("love calculator")
print("Welcome to the Love Calculator")
name1 = input("what is your name?\n")
name2 = input("What is his/her name?\n ")
lower_case_name = name1.lower()
lower_case_name2 = name2.lower()
combined_string = lower_case_name + lower_case_name2

T = combined_string.count("t")
R = combined_string.count("r")
U = combined_string.count("u")
E = combined_string.count("e")
num1 = str(T + R + U + E)
L = combined_string.count("l")
O = combined_string.count("o")
V = combined_string.count("v")
E = combined_string.count("e")
num2 = str(L + O + V + E)
loving_number = (num1 + num2)
print(loving_number)
if loving_number <= str(10) or loving_number >= str(90):
    print(f"your score is {loving_number} You both are like coke and mentos, ")
elif str(40) < loving_number < str(50):
    print(f"your score is {loving_number}, you are good together")
else:
    print(f" your score is {loving_number}")








# Treasure Island




