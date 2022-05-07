from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data") as data:
            self.high_score = int(data.read())
        self.up()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 280)
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   HIGH SCORE: {self.high_score}", move=True, align=ALIGNMENT, font=FONT)
        self.goto(0, 280)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # with open("data", mode="w") as new_score:
            #     new_score.write(f"{self.high_score}")

        self.score = 0
        self.scoreboard()







