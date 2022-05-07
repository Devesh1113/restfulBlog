from tkinter import *


def convert_into_km():
    answer = int(entry1.get())
    miles = 1.609 * answer
    label4.config(text=miles)


window = Tk()
window.title("Widget Examples")
window.config(padx=20, pady=20)

entry1 = Entry(width=10)
entry1.grid(column=1, row=0)

label1 = Label(text="Miles", font=("Consolas", 12, "normal"))
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=("Consolas", 12, "normal"))
label2.grid(column=0, row=1)

label3 = Label(text="Km", font=("Consolas", 12, "normal"))
label3.grid(column=2, row=1)

label4 = Label(text="0", font=("Consolas", 12, "normal"))
label4.grid(column=1, row=1)

button = Button(text="Calculate", command=convert_into_km)
button.grid(column=1, row=2)


window.mainloop()
