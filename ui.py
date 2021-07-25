from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quetion_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50 )

        true_button = PhotoImage(file="images/true.png")
        false_button = PhotoImage(file="images/false.png")

        self.button_T = Button(image=true_button, highlightthickness=0, command=self.true_func)
        self.button_T.grid(row=2, column=1)

        self.button_F = Button(image=false_button, highlightthickness=0, command=self.false_func)
        self.button_F.grid(row=2, column=0)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quetion_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quetion_text, text="You've reached the end of the quiz.")
            self.button_T.config(state="disabled")
            self.button_F.config(state="disabled")


    def true_func(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_func(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)
