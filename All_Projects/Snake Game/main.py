from turtle import Screen, Turtle
from snake import Snake
from Food import Food
from Score import Score
from boundary import Boundary
import time


show_SOMETHING = Turtle()
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
boundary = Boundary()

snake_body = Snake()
snake_food = Food()
score = Score()


my_screen.listen()
my_screen.onkey(key="Up", fun=snake_body.move_upward)
my_screen.onkey(key="Down", fun=snake_body.move_downward)
my_screen.onkey(key="Right", fun=snake_body.move_rightward)
my_screen.onkey(key="Left", fun=snake_body.move_leftward)

my_screen.update()

is_snake_move = True
while is_snake_move:
    my_screen.update()
    time.sleep(0.1)

    snake_body.move()
    if snake_body.segments[0].distance(snake_food) < 15:
        score.score += 1
        snake_food.refresh()
        snake_body.extend()
        score.scoreboard()

    if snake_body.segments[0].xcor() > 290 or snake_body.segments[0].xcor() < -280 or \
            snake_body.segments[0].ycor() > 279 or snake_body.segments[0].ycor() < -290:
        score.reset()
        snake_body.reset()

    for segments in snake_body.segments[1:]:
        if snake_body.segments[0].distance(segments) < 10:
            score.reset()
            snake_body.reset()


my_screen.exitonclick()
