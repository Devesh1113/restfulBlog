from tkinter import *
import pandas
from random import *
BACKGROUND_COLOR = "#B1DDC6"


# Data
my_data = pandas.read_csv("data/french_words.csv")
data_to_be_used = my_data.to_dict(orient="records")
chosen_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_to_be_used = original_data.to_dict(orient="records")
else:
    data_to_be_used = data.to_dict(orient="records")


def is_known():
    data_to_be_used.remove(chosen_word)
    data = pandas.DataFrame(data_to_be_used)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_word()


def change_word():
    global chosen_word, flip_timer
    window.after_cancel(flip_timer)
    chosen_word = choice(data_to_be_used)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=chosen_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_cards)


def flip_cards():
    global chosen_word
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(word, text=chosen_word["English"], fill="white")


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_cards)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="../flash-card-project-start/images/card_back.png")
card_front = PhotoImage(file="../flash-card-project-start/images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Images
wrong_button_image = PhotoImage(file="../flash-card-project-start/images/wrong.png")
right_button_image = PhotoImage(file="../flash-card-project-start/images/right.png")

# Buttons
wrong = Button(image=wrong_button_image, highlightthickness=0, command=change_word)
wrong.grid(row=1, column=0)
right = Button(image=right_button_image, highlightthickness=0, command=is_known)
right.grid(row=1, column=1)

change_word()
window.mainloop()
