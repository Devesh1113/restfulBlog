from tkinter import *


def button_clicked():
    my_label.config(text="button got clicked")


def my_input():
    answer = my_input.get()
    my_label.config(text=answer)


def button_2():
    my_label.config(text="button_clicked")


windows = Tk()
windows.title("GUI")
windows.minsize(width=300, height=200)
# making more spacious
windows.config(padx=100, pady=200)

# Label
my_label = Label(text="Email", font=("Consolas", 12, "normal"))
# my_label.place(x=15, y=56)
my_label.grid(column=1, row=1)
# change something in a label
# my_label["text"] = "new_text"
# my_label.config(text="new_text")

# Buttons
button = Button(text="Click me", command=my_input)
button.grid(column=2, row=2)
# making widget more spacious
button.config(padx=5, pady=7)

button2 = Button(text="Click", command=button_2)
button2.grid(column=3, row=1)

# Entry component
my_input = Entry(width=20)
# my_input.place(x=78, y=58)
my_input.grid(column=8, row=12)

windows.mainloop()


