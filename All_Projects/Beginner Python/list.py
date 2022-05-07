row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
print(horizontal)
vertical = int(position[1])

devesh = map[vertical - 1]
devesh[horizontal - 1] = "x"

user_cards.append(deal_card())
computer_cards.append(deal_card())
if user_score > 21:
    game_over = True
    print(f"Your Cards: {user_cards}, Final score: {user_score}")
    print(f"Computer's all cards: {computer_cards}, Final score: {computer_score}")
    print("you went over.You Lose")
if user_score < 21:
    game_over = False
    if user_score < computer_score:
        game_over = True
        print(f"Your Cards: {user_cards}, Final score: {user_score}")
        print(f"Computer's all cards: {computer_cards}, Final score: {computer_score}")
        print("computer win")
    elif user_score > computer_score:
        print(f"Your Cards: {user_cards}, Final score: {user_score}")
        print(f"Computer's all cards: {computer_cards}, Final score: {computer_score}")
        print("You win")


#BlackJack Game
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card

def calculate_score(type_of_cards):
    if sum(type_of_cards) == 21 and len(type_of_cards) == 2:
        return 0
    elif 11 in type_of_cards and sum(type_of_cards) > 21:
        type_of_cards.remove(11)
        type_of_cards.append(1)

    else:
        return sum(type_of_cards)
user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = int(calculate_score(user_cards))
computer_score = int(calculate_score(computer_cards))
game_over = False
while not game_over:
    user_score = (calculate_score(user_cards))
    computer_score = (calculate_score(computer_cards))
    print(f"Your Cards: {user_cards}, Current score: {user_score}")
    print(f"Computer's first hand: {computer_cards} ")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True

    else:
        choice = input("Do you want to draw another card. Type 'y' or 'n' ")
        if choice == "y":
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
            game_over = False















#import random
#names_string = input("give me the names who are playing  ")
#names = names_string.split()
#length = int(len(names))

#given_names = random.randint(1, length - 1)
#person_who_is_going_to_pay = (names[given_names])
#print(f"{person_who_is_going_to_pay} is going to pay today")



