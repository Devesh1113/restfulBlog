import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_upwards, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()
    if turtle.ycor() >= 290:
        turtle.get_back()
        scoreboard.scoreboard()
        cars.increase_speed()

    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            turtle.show_game_over()

screen.exitonclick()