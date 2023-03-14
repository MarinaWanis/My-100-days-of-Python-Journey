from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class GraphicalInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Qiuzzler")
        self.window.config(padx=30, pady=30, bg= THEME_COLOR)
        self.user_score = 0

        #---------------------------Score Label----------------------------------------------------------#
        self.score = Label(text= f"Score: 0", bg= THEME_COLOR, fg="white", font= ("Couirer", 15, "normal"))
        self.score.grid(column =1, row=0)

        #------------------------------Canvas------------------------------------------------#
        self.canvas = Canvas(width= 300, height= 250, bg= "white", highlightthickness=0)

        self.question_text =self.canvas.create_text(150,115,text="Test", font=("Arial", 20, "italic"), fill= THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #-------------------------True button-----------------------------#
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, bg= THEME_COLOR, highlightthickness=0,command = self.choose_true)
        self.true_button.grid(column=0, row= 2)

        # -------------------------False button-----------------------------#
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, bg=THEME_COLOR, highlightthickness=0, command = self.choose_false)
        self.false_button.grid(column=1, row= 2)
        self.display_question()

        self.window.mainloop()

    def display_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your Final score is {self.quiz.score} out of 10. ")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

    def choose_true(self):
        self.add_color(self.quiz.check_answer('True'))

    def choose_false(self):
        self.add_color(self.quiz.check_answer('False'))

    def add_color(self, is_answer_right):
        if is_answer_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text,fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.display_question)



