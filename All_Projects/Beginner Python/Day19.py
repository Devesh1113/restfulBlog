from turtle import Turtle, Screen
import random
is_race_on = False
color = ["red", "blue", "orange", "yellow", "violet", "green"]
screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter the colour")

all_turtle_list = []
y = [150, 100, 50, 0, -50, -100]
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.up()
    new_turtle.goto(x=-240, y=y[i])
    all_turtle_list.append(new_turtle)


if choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle.pencolor()
            if choice == winner_turtle:
                print(f"You Won. {choice } is the winner!")
            else:
                print(f"You chose {choice}. {winner_turtle} Won the race, You lose! ")
        else:
            random_distance = random.randint(0, 10)
            turtle.speed(6)
            turtle.fd(random_distance)






# tommy.color(color[1])
# tommy.up()
# tommy.goto(x=-240, y=100)
#
# sheru.color(color[2])
# sheru.up()
# sheru.goto(x=-240, y=50)
#
# ronny.color(color[3])
# ronny.up()
# ronny.goto(x=-240, y=0)
#
# johncena.color(color[4])
# johncena.up()
# johncena.goto(x=-240, y=-50)
#
# sonty.color(color[5])
# sonty.up()
# sonty.goto(x=-240, y=-100)



# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.back(10)
#
#
# def counter_clockwise():
#     heading = tim.heading() + 18
#     tim.setheading(heading)
#
#
# def clockwise():
#     heading = tim.heading() - 18
#     tim.setheading(heading)
#
#
# def clear():
#     tim.reset()
#
#
# screen.listen()
# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=move_backward, key="s")
# screen.onkey(fun=counter_clockwise, key="a")
# screen.onkey(fun=clockwise, key="d")
# screen.onkey(fun=clear, key="c")
screen.exitonclick()
