import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

list_of_word = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(list_of_word)
length = len(chosen_word)

lives = 6

display = ["_"] * length

while display != True:
    guess = input("Enter the random letter\n").lower()

    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            display = True
            print("You Lose")
        print(display)

    if "_" not in display:
        display = True
        print(" Congratulations! You Win")

    print(stages[lives])



