# Local Scope: can only access name function if its inside another function called my_name.
def my_name():
    def name():
        name = "Devesh"
        print(name)
        name()
my_name()

# Global Scope: now i can access this variable from anywhere whether its outside a function or inside
name = "devesh"
def another_name():
    print(name)
print(name)

# Block Scope: in this case the variable is inside the if statment but it doesn't matter i can also access it from outside
if 5 > 3:
   surname = "nothing"
   print(surname)
print(surname)

# Modify a global scope: to modify a global scope in a local scope we have to add a keyword called "global"
enimies = 1
def kill_enimies():
    global enimies
    enimies += 1
    print(f" The enimies are {enimies}")
kill_enimies()
print(enimies)

# Day 12 Project
logo = """
███    ██ ██    ██ ███    ███ ██████  ███████ ██████       ██████  ██    ██ ███████ ███████ ███████ ██ ███    ██  ██████       ██████   █████  ███    ███ ███████ 
████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██     ██       ██    ██ ██      ██      ██      ██ ████   ██ ██           ██       ██   ██ ████  ████ ██      
██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████      ██   ███ ██    ██ █████   ███████ ███████ ██ ██ ██  ██ ██   ███     ██   ███ ███████ ██ ████ ██ █████   
██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██     ██    ██ ██    ██ ██           ██      ██ ██ ██  ██ ██ ██    ██     ██    ██ ██   ██ ██  ██  ██ ██      
██   ████  ██████  ██      ██ ██████  ███████ ██   ██      ██████   ██████  ███████ ███████ ███████ ██ ██   ████  ██████       ██████  ██   ██ ██      ██ ███████ 
"""
print(logo)
import random
computer_num = random.randint(1, 100)
print(computer_num)
print("Welcome to the Number Guessing Game")
print("I'm thinking a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' :  ").lower()
def new_difficalty():
    if difficulty == "easy":
        return 10
    else:
        return 5
my_difficulty = new_difficalty()

if difficulty == "easy":
    print(f"You have {my_difficulty} attempts remaining to guess the number")
else:
    print(f"You have {my_difficulty} attempts remaining to guess the number")

is_game_over = False
while not is_game_over :
    guess = int(input("Make a guess:  "))
    if guess > computer_num:
        my_difficulty -= 1
        if my_difficulty == 0:
            print("You have run out of guesses. You lose")
            break
        else:
            print("Too high")
            print("Guess again")
            print(f"You have {my_difficulty} attempts left.")
    elif guess < computer_num:
        my_difficulty -= 1
        if my_difficulty == 0:
            print("You have run out of guesses. You lose")
            break
        else:
            print("Too low")
            print("Guess again")
            print(f"You have {my_difficulty} attempts left.")
    else:
        print(f" You got it! The answer was {guess}.")
        break
