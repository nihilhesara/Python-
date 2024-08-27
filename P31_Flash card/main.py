from tkinter import *
import os
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)  # Choose a random card from the list
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")  # Display the French word
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=current_card["English"], fill="White")
    canvas.itemconfig(card_background, image=card_back_image)

window = Tk()
window.title("Flash crad")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title = canvas.create_text(400,150,text="Title", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unkonwn_button = Button(image=cross_image, command=next_card)
unkonwn_button.grid(column=0,row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=next_card)
known_button.grid(column=1,row=1)

next_card()

window.mainloop()