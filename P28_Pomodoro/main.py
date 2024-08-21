from tkinter import *
import os 

# Path to the image file
image_path = os.path.join("P28_Pomodoro", "tomato.png")

# ---------------------------- CONSTANTS ------------------------------- #
# Color constants used in the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Font name used for labels
FONT_NAME = "Courier"

# Timing constants in minutes
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variables to track the number of repetitions and the timer reference
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
# Function to reset the timer
def reset_timer():
    # Cancel the ongoing timer
    window.after_cancel(timer)
    
    # Reset the timer text, title label, and check marks
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_mark.config(text="")
    
    # Reset the repetition counter
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
# Function to start the timer for work, short break, or long break
def start_timer():
    global reps
    reps += 1  # Increment the repetition counter

    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine whether it's time for work, a short break, or a long break
    if reps % 2 == 1:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)  # Set the title to "Work"
        
        # Update check marks for completed work sessions
        marks = ""
        work_session = reps // 2
        for i in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)

    elif reps == 8:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)  # Set the title to "Break" with red color for long break
    else:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)  # Set the title to "Break" with pink color for short break

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Function to handle the countdown
def count_down(count):
    # Calculate minutes and seconds from the total count
    count_min = count // 60
    count_sec = count % 60

    # Formatting the seconds to always show two digits
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <= 9:
        count_sec = f"0{count_sec}"

    # Update the timer text on the canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # Continue the countdown if there's time left
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Call count_down every 1 second
    else:
        start_timer()  # Start the next timer when the countdown finishes

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title label at the top
title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

# Canvas to display the tomato image and timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image_path)  # Load the tomato image
canvas.create_image(100, 112, image=tomato_img)  # Position the image in the center of the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Timer text in the middle of the image
canvas.grid(column=1, row=1)

# Start button to initiate the timer
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button to reset the timer
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Label to display check marks for completed work sessions
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

# Start the main event loop of the Tkinter application
window.mainloop()