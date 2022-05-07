from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.up()
        self.hideturtle()
        self.color("black")
        self.goto(-295, 265)
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(arg=f"LEVEL: {self.score}", move=True, align="Left", font=FONT)
        self.score += 1
        self.goto(-295, 265)


