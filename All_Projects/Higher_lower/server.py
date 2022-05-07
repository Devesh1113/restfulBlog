from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 9)


@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp'>"


@app.route("/<int:number>")
def number_guessing(number):
    if number == random_num:
        return "<h1 style = 'color: green'>You found me!</h1>" \
               "<img src='https://i.giphy.com/media/4T7e4DmcrP9du/giphy.webp'>"
    elif number > random_num:
        return "<h1 style = 'color: green'>Too High!</h1>" \
               "<img src='https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp'>"
    else:
        return "<h1 style = 'color: green'>Too Low!</h1>" \
               "<img src='https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp'>"


if __name__ == "__main__":
    app.run(debug=True)
