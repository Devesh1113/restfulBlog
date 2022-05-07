from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.shape("turtle")
        x = random.randint(-13, 13) * 20
        y = random.randint(-13, 13) * 20
        self.goto(x, y)

    def refresh(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.goto(x, y)

