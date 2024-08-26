from tkinter import *
import os

BACKGROUND_COLOR = "#B1DDC6"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

window = Tk()
window.title("Flash crad")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.create_text(400,150,text="Title", font=("Ariel",40,"italic"))
canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unkonwn_button = Button(image=cross_image)
unkonwn_button.grid(column=0,row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image)
known_button.grid(column=1,row=1)

window.mainloop()