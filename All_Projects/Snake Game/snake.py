from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

positions = [(0, 0), (-20, 0), (-40, 0)]
move = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body = Turtle()
        snake_body.shape("square")
        snake_body.color("white")
        snake_body.up()
        snake_body.goto(position)
        self.segments.append(snake_body)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for snake in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake - 1].xcor()
            new_y = self.segments[snake - 1].ycor()
            self.segments[snake].goto(new_x, new_y)
        self.segments[0].fd(move)

    def move_rightward(self):
        move_rightward = self.segments[0]
        if move_rightward.heading() != LEFT:
            move_rightward.seth(RIGHT)
            move_rightward.heading()

    def move_upward(self):
        move_upward = self.segments[0]
        if move_upward.heading() != DOWN:
            move_upward.seth(UP)
            move_upward.heading()

    def move_leftward(self):
        move_leftward = self.segments[0]
        if move_leftward.heading() != RIGHT:
            move_leftward.seth(LEFT)
            move_leftward.heading()

    def move_downward(self):
        move_downward = self.segments[0]
        if move_downward.heading() != UP:
            move_downward.seth(DOWN)
            move_downward.heading()

    def show_game_over(self):
        ALIGNMENT = "center"
        FONT = ("Arial", 12, "normal")
        show_SOMETHING = Turtle()
        show_SOMETHING.up()
        show_SOMETHING.hideturtle()
        show_SOMETHING.color("white")
        show_SOMETHING.goto(0, 0)
        show_SOMETHING.write(arg="GAME OVER!", move=True, align=ALIGNMENT, font=FONT)

    def detect_collision(self):
        for i in range(1, self.segments[-1]):
            return i

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()


