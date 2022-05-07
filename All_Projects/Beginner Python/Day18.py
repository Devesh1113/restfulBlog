import turtle
from turtle import Turtle, Screen
import random

# Hirst painting

devesh = Turtle()
devesh.shape("classic")
devesh.color("blue")
devesh.speed(0)
turtle.colormode(255)
devesh.hideturtle()

num1 = 20
num2 = 0
width = int(input("what should be the width of dots? "))
height = int(input("what should be the height of dots? "))
mine = width * height

for i in range(0, mine, width):
    num2 += 1
    devesh.up()
    devesh.home()
    devesh.setpos(-350, -250 + (num1 * num2))

    for j in range(0, width):
        colors_to_be_used = [(229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50),
                             (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227),
                             (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134)]
        random_color = random.choice(colors_to_be_used)
        devesh.dot(15, random_color)
        devesh.up()
        devesh.forward(num1)
        devesh.down()


my_screen = Screen()
my_screen.exitonclick()


# for i in range(20):
#     devesh.pencolor("gold")
#     devesh.speed(10)
#     devesh.forward(5)
#     devesh.up()
#     devesh.forward(5)
#     devesh.down()
# devesh.pencolor("red")
# def draw(num_side):
#     for _ in range(num_side):
#         angle = 360 // num_side
#         devesh.forward(50)
#         devesh.left(angle)
#         devesh.forward(50)
#
# for i in range(3, 11):
#     draw(i)

# for _ in range(4):
#     devesh.forward(50)
#     devesh.right(90)
#
# devesh.right(45)
# devesh.up()
# devesh.forward(10)
# devesh.down()
# devesh.left(45)
# for i in range(4):
#     devesh.forward(35)
#     devesh.rt(90)

# for _ in range(4):
#     devesh.forward(50)
#     devesh.right(90)
#     devesh.forward(50)
# devesh.pencolor("Yellow")
# devesh.width(10)
# devesh.speed(0)
# devesh.setpos(100, 100)
# devesh.setx(50)
# devesh.sety(46)
# devesh.dot(45, "black")
# devesh.xcor()

# my_tuple = (1, 3, 8)

#
#

#
#
# directions = [0, 90, 180, 270]
# way = [devesh.forward(35), devesh.backward(35)]
# for i in range(250):
#     devesh.speed(0)
#     devesh.width(10)
#     devesh.pencolor(random_color())
#     devesh.forward(35)
#     devesh.seth(random.choice(directions))
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_tuple = (r, g, b)
#     return my_tuple
#
#
# for i in range(0, 72):
#     devesh.speed(0)
#     devesh.pencolor(random_color())
#     devesh.circle(100)
#     devesh.left(5)


# Hirst Spot Painting
# import colorgram
#
# colors =colorgram.extract('MY_image.jpg', 20)
#
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     more_colors = (r, g, b)
#     rgb.append(more_colors)
# print(rgb)