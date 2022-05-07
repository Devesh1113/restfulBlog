from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(). __init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.seth(90)
        self.heading()
        self.goto(0, -280)

    def move_upwards(self):
        self.fd(MOVE_DISTANCE)

    def get_back(self):
        self.goto(0, -280)

    def show_game_over(self):
        ALIGNMENT = "center"
        FONT = ("Arial", 12, "normal")
        show_SOMETHING = Turtle()
        show_SOMETHING.up()
        show_SOMETHING.hideturtle()
        show_SOMETHING.color("Black")
        show_SOMETHING.goto(0, 0)
        show_SOMETHING.write(arg="GAME OVER!", move=True, align=ALIGNMENT, font=FONT)



