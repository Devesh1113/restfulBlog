from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Consolas"
WORK_MIN = 0.15
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_time():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    label1.config(text="Timer", fg=GREEN)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label1.config(text="Break", fg=PINK)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        label1.config(text="Break", fg=RED)
        count_down(short_break_sec)
    else:
        label1.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = int(count / 60)
    count_sec = int(count % 60)
    if count_sec == 0:
        count_sec = "00"
    if 1 <= int(count_sec) < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        label2.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
text = "✔"

window = Tk()
window.title("Pomodoro Game")
window.config(padx=100, pady=50, bg=YELLOW)

label1 = Label(text="Timer", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)
label1.grid(column=1, row=0)

label2 = Label(text=" ", font=(FONT_NAME, 12, "normal"), fg=GREEN, bg=YELLOW)
label2.grid(column=1, row=3)

button1 = Button(text="Start", width=8, command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", width=8, command=reset_time)
button2.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
