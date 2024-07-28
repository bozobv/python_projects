THEME_COLOR = "#375362"
from os import set_inheritable
import tkinter as tk

FONT_SCORE = ("Arial", 20, "bold")
FONT_QUESTION = ("Arial", 17, "italic")
from quiz_brain import QuizBrain

class QuizInterface:
    
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg=THEME_COLOR)
        
        self.img_false = tk.PhotoImage(file="day34/images/false.png")
        self.img_true = tk.PhotoImage(file="day34/images/true.png")
        
        self.canvas = tk.Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question = self.canvas.create_text(150, 
                                                80,
                                                text="test", 
                                                font=FONT_QUESTION, 
                                                fill=THEME_COLOR,
                                                width=280)
        
        self.bt_true = tk.Button(self.window, image=self.img_true, highlightthickness=0)
        self.bt_true.grid(row=2, column=0, padx=20, pady=20)
        self.bt_false = tk.Button(self.window, image=self.img_false, highlightthickness=0)
        self.bt_false.grid(row=2, column=1, padx=20, pady=20)
        
        self.bt_true.configure(command=self.tip_true)
        self.bt_false.configure(command=self.tip_false)
        
        self.lb_score = tk.Label(self.window, text="Score: 0", font=FONT_SCORE, bg=THEME_COLOR, fg="white")
        self.lb_score.grid(row=0, column=1, padx=20, pady=20)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.lb_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz. Congrats!")
            self.bt_false.config(state="disabled")
            self.bt_true.config(state="disabled")

        
    def tip_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
    
    def tip_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, rightness):
        print(rightness)
        if rightness:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
            
        self.window.after(1000, self.get_next_question)


