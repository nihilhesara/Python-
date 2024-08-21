from tkinter import *
import os 
image_path = os.path.join("P28_Pomodoro", "tomato.png")

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

"""
----------------- AFTER METHOD ---------------------- 
def say_something(thing):
    print(thing)

window.after(1000,say_something,"hello")
# (waiting time in miliseconds, funciton name , value or values that you pass to the function )"""

def count_down(count):

    count_min = count // 60
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    
    elif count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,count_down,count -1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # highlightthickness=0 get rid of the border
tomato_img = PhotoImage(file=image_path)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔",fg=GREEN, bg=YELLOW)
check_mark.grid(column=1,row=3)

window.mainloop()
