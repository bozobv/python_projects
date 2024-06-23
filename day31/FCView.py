import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
IMG_CARD_BACK = "images/card_back.png"
IMG_CARD_FRONT = "images/card_front.png"
IMG_CORRECT = "images/right.png"
IMG_WRONG = "images/wrong.png"

class FCView:
    
    def __init__(self, window):
        
        window.title("Tanuló kártyák")
        
        window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
        
        self.card_front_img = tk.PhotoImage(file=IMG_CARD_FRONT)
        self.card_back_img = tk.PhotoImage(file=IMG_CARD_BACK)
        self.img_wrong = tk.PhotoImage(file=IMG_WRONG)
        self.img_correct = tk.PhotoImage(file=IMG_CORRECT)

        self.canvas = tk.Canvas(width=800, height=526)
        
        self.card_background = self.canvas.create_image(400, 263, image=self.card_front_img)
        #canvas.itemconfig(self.card_background, image=self.card_front_img)
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.card_language = self.canvas.create_text(400, 150, text="test", font=FONT_LANGUAGE)
        self.card_word = self.canvas.create_text(400, 263, text="test", font=FONT_WORD)

        self.card_language_1 = "test"
        self.card_language_2 = "test2"

        self.bt_success = tk.Button(window, image=self.img_correct, highlightthickness=0)
        self.bt_success.grid(row=1, column=0)
        self.bt_fail = tk.Button(window, image=self.img_wrong, highlightthickness=0)
        self.bt_fail.grid(row=1, column=1)
        
        window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.timer_id = None
        self.window = window
        
    def set_controller(self, controller):
        self.controller = controller
        self.bt_success.configure(command=controller.correct_press)
        self.bt_fail.configure(command=controller.incorrect_press)
        
    def set_languages(self, language_1, language_2):
        self.card_language_1 = language_1
        self.card_language_2 = language_2  
        
    def set_new_words(self, word1, word2):
        self.word_language_1 = word1
        self.word_language_2 = word2
            
    def update_word_language_1(self):
        self.canvas.itemconfig(self.card_background, image=self.card_front_img)
        self.canvas.itemconfig(self.card_language, text=self.card_language_1, fill="black")
        self.canvas.itemconfig(self.card_word, text=self.word_language_1, fill="black")
        #self.window.after(3000)
        
    def update_word_language_2(self):
        self.canvas.itemconfig(self.card_background, image=self.card_back_img)
        self.canvas.itemconfig(self.card_language, text=self.card_language_2, fill="white")
        self.canvas.itemconfig(self.card_word, text=self.word_language_2, fill="white")   
        self.timer_id = None  
        
    def next_words(self, word1, word2): 
        if self.timer_id is not None:
            self.window.after_cancel(self.timer_id)
            self.timer_id = None
            
        self.set_new_words(word1, word2)
        self.update_word_language_1()
        self.timer_id = self.window.after(3000, func=self.update_word_language_2)
        
    def on_closing(self):
        self.controller.save()
        self.window.destroy()

        