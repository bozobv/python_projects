from os import terminal_size
import tkinter as tk
from tkinter.constants import Y
import math
from typing import Text

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECS_IN_MINUTE = 60
reps = 0
timer = None

pomodoro_stages ={
    "WORK 1" : WORK_MIN,
    "BREAK 1" : SHORT_BREAK_MIN,
    "WORK 2" : WORK_MIN,
    "BREAK 2" : SHORT_BREAK_MIN,
    "WORK 3" : WORK_MIN,
    "BREAK 3" : SHORT_BREAK_MIN,
    "WORK 4" : WORK_MIN,
    "BREAK 4" : LONG_BREAK_MIN,
}
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    lb_pipe.configure(text="kezdj dolgozni")
    lb_title.configure(text="Időgenyó")
    canvas.itemconfig(timer_text, text="00:00")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    
    keys = list(pomodoro_stages.keys())
    
    count_down(pomodoro_stages[keys[reps]] * SECS_IN_MINUTE)
    lb_title.configure(text=keys[reps])
    reps += 1
    
    pipes = '✓' * math.floor((reps+1) / 2)
    lb_pipe.configure(text=pipes)

    if reps > 7:
        reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min=f"0{count_min}"
        
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") 
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count - 1 )
        
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#fg==foreground --> GREEN

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = tk.PhotoImage(file="day28/tomato.png")

lb_title = tk.Label(window, text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
lb_title.grid(column=1, row=0)

lb_pipe = tk.Label(window, text="✓", bg=YELLOW, fg=GREEN)
lb_pipe.grid(column=1, row=3)

bt_start = tk.Button(window, text="Start", command=start_timer)
bt_start.grid(column=0, row=2)

bt_reset = tk.Button(window, text="Reset", command=reset_timer)
bt_reset.grid(column=2, row=2)


canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


window.mainloop()