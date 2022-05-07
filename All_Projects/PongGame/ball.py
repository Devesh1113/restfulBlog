from turtle import Turtle
from paddle import Paddle
import random
ANGLE = 45
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        new_y = self.ycor() + self.y
        new_x = self.xcor() + self.x
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()






