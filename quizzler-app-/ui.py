import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quiz Game")
        self.windows.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = tkinter.Label(text="Score: 0", font=("arial", 10, "normal"))
        self.score.grid(column=1, row=0)
        self.score.config(background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some text question", width=280, font=("arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.tick_img = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=self.tick_img, highlightthickness=0, borderwidth=0, command=self.right_pressed)
        self.tick_button.grid(column=0, row=2)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, borderwidth=0, command=self.left_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The End")
            self.tick_button.config(state=DISABLED)
            self.wrong_button.config(state=DISABLED)

    def right_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def left_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.update()
        self.windows.after(1000, self.get_next_question())

