from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    scoreboard = Score()
    time.sleep(0.1)
    screen.update()
    ball.speed(1)
    ball.move()
    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 385:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -385:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()






