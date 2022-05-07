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
    if 11 in type_of_cards and sum(type_of_cards) > 21:
        type_of_cards.remove(11)
        type_of_cards.append(1)

    return sum(type_of_cards)

def compare_cards():
    if calculate_score(user_cards) > 21:
        print(f"Your Final Hand: {user_cards}, Final Score: {calculate_score(user_cards)}")
        print(f"Computer's Final Card: {computer_cards}, Final Score: {calculate_score(computer_cards)} ")
        print("You lose")
    elif calculate_score(computer_cards) <= 21:
        if calculate_score(user_cards) > calculate_score(computer_cards):
            print(f"Your Final Hand: {user_cards}, Final Score: {calculate_score(user_cards)}")
            print(f"Computer's Final Card: {computer_cards}, Final Score: {calculate_score(computer_cards)} ")
            print("You Win")

        if calculate_score(user_cards) < calculate_score(computer_cards):
            print(f"Your Final Hand: {user_cards}, Final Score: {calculate_score(user_cards)}")
            print(f"Computer's Final Card: {computer_cards}, Final Score: {calculate_score(computer_cards)} ")
            print("You Lose")
    elif calculate_score(computer_cards) > 21:
        print(f"Your Final Hand: {user_cards}, Final Score: {calculate_score(user_cards)}")
        print(f"Computer's Final Card: {computer_cards}, Final Score: {calculate_score(computer_cards)} ")
        print("You Win")

def check_computer_score():
    if calculate_score(computer_cards) < 17:
        while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())

wanna_play = input("Do you want to play a game of blackjack? Type 'y' or 'n'  ").lower()

if wanna_play == "y":
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over:
        print(f"Your Current Hand: {user_cards}, Current Score: {calculate_score(user_cards)}")
        print(f"Computer's First Card: {computer_cards[0]}")
        choice_of_user = input("Type 'y' to draw another Card or 'n' to pass!  ").lower()
        if choice_of_user == "y":
            for i in range(1):
                user_cards.append(deal_card())
            if calculate_score(user_cards) > 21:
                check_computer_score()
                compare_cards()
                is_game_over = True
            elif calculate_score(user_cards) <= 21:
                is_game_over = False
        if choice_of_user == "n":
            check_computer_score()
            compare_cards()
            is_game_over = True

else:
    print("Ok BYe HAve a NIce DaY")


