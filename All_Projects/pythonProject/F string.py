# example
score = 0
height = 1.8
isWinning = True
# F string
print(f"your score is {score} your height is {height} you are winning is {isWinning}")
# otherwise we had to follow diffrent expressions
print("your score is " + str(score) + "your height is " + str(height) + " you are winning is " + str(isWinning) )

# Coding Exercise
age = input("what's your age  ")
x =(90 - int(age))* 365
y =(90 - int(age))* 52
z =(90 - int(age))* 12
print(f"you have {x} days , {y} weeks , {z} days left ")
