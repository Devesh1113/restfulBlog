from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"


class UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score:0", font=("Arial", 15, "italic"), bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("Arial", 15, "italic"),
                                                     fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_image = PhotoImage(file="../quizzler-app-start/images/true.png")
        self.true_button = Button(image=true_button_image,  highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(row=2, column=0)

        false_button_image = PhotoImage(file="../quizzler-app-start/images/false.png")
        self.false_button = Button(image=false_button_image,  highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the Quiz.")
            self.canvas.config(bg="white")
            self.true_button.destroy()
            self.false_button.destroy()

    def check_answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)






