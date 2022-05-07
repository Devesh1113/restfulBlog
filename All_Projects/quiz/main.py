import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Name")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
num = 0
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

guessed_states = []
while num <= 50:
    answer_name = (screen.textinput(title=f"Correct State: {num}/50", prompt="What's another state name?")).title()
    if answer_name == "Exit":
        states_to_learn =[state for state in state_list if state not in guessed_states]
        not_guessed_states = pandas.DataFrame(states_to_learn)
        not_guessed_states.to_csv("states_to_learn.csv")
        break
    if answer_name in state_list:
        guessed_states.append(answer_name)
        num += 1
        row = data[data.state == answer_name]
        x = int(row.x)
        y = int(row.y)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(x, y)
        state_name.write(arg=answer_name, align="center", font=("courier", 9, "normal"))





