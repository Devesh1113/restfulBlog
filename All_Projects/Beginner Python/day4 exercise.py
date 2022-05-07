
import random
rock = '''

    _______

---'   ____)

      (_____)

      (_____)

      (____)

---.__(___)

'''



paper = '''

    _______

---'   ____)____

          ______)

          _______)

         _______)

---.__________)

'''



scissors = '''

    _______

---'   ____)____

          ______)

       __________)

      (____)

---.__(___)

'''
game = [rock, paper, scissors]
choosing = int(input("Choose Rock Paper or Scissors  Type 0 for rock, 1 for paper and 2 for scissors   " ))
print(f"you chose {game[choosing]}")


computer_choice = int(random.randint(0, 2))
print(f" Computer chose {game[computer_choice]}")

if choosing == 0:
    if computer_choice == 0:
        print("game Tied")
    if computer_choice == 1:
        print("You Lose")
    if computer_choice == 2:
        print("you Win")

if choosing == 1:
    if computer_choice == 0:
        print("You win")
    if computer_choice == 1:
        print("game Tied")
    if computer_choice == 2:
        print("you lose")

if choosing == 2:
    if computer_choice == 0:
        print("You Losee")
    if computer_choice == 1:
        print("You win")
    if computer_choice == 2:
        print("Game Tied")

# Fizz Buzz Game

for my_num in range(1, 101):

    if my_num % 3 == 0 and my_num % 5 == 0:
        print("Fizz Buzz")
    if my_num % 5 == 0:
        print("fizz")
    if my_num % 3 == 0:
        print("buzz")
    else:
        print(my_num)









# sum of even numbers
num = 0
for number in range(1, 101):
    if number <= 50:
     num += (number * 2)
print(num)


sum_of_number = 0
for number in range(1, 51):
    sum_of_number += number
    print(sum_of_number)

#Score of different students
student_scores = input("Type the list of scores\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

score = 0
for highest_score in student_scores:
    if highest_score > score:
        score = highest_score
print(f"The highest score is {score}")

#Height of the students
student_heights = input("type the height of students using space!\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


mine = 0
for height in student_heights:
    mine += height
print(student_heights)

no_of_students = 0
for number in student_heights:
    no_of_students += 1


avg = mine / no_of_students
print(f" {avg} is average height of the class")

vegetables = ["Tomato", "potato", "brinjal"]

















