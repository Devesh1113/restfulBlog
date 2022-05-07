from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(0, 275)
        self.shape("classic")
        self.pencolor("white")
        self.down()
        self.fd(290)
        self.rt(90)

        self.fd(565)
        self.rt(90)
        self.fd(587)
        self.rt(90)
        self.fd(565)
        self.rt(90)
        self.fd(297)





