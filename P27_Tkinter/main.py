from tkinter import *

window = Tk()
window.title("My first GUI program")    # Window title
window.minsize(width=500, height=300)    # Minimum size of the window

# Create the label (It displays now)
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack() # my_label.pack(side="left")  # Setting the label in the window (Default side is center)

my_label["text"] = "New text"  # Modify the text of the label using dictionary-like indexing
my_label.config(text="New Text")  # Another way to modify the label text using the config method

def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label.config(text= new_text)

# Button
button = Button(text="Click me", command=button_clicked) # we put name of the function in command attribute 
button.pack()

# Entry (create a text box)
input = Entry(width=10)
input.pack()
print(input.get())

# ______________________________________________________________________________________________________________________


window.mainloop()  # Keep the screen
