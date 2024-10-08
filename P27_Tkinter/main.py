from tkinter import *   # Must know about .pack, .place and .grid

window = Tk()
window.title("My first GUI program")    # Window title
window.minsize(width=500, height=300)    # Minimum size of the window
window.config(padx=20,pady=20)          # Add padding to the window 

# Create the label (It displays now)
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New text"  # Modify the text of the label using dictionary-like indexing
my_label.config(text="New Text")  # Another way to modify the label text using the config method
my_label.pack() # my_label.pack(side="left")  # Setting the label in the window (Default side is center)

def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label.config(text= new_text)

# Button
button = Button(text="Click me", command=button_clicked) # we put name of the function in command attribute 
button.place(x=0 , y=0) # In place we can give x value and the y value of  the place

# Entry (create a text box)
input = Entry(width=10)
print(input.get())
input.pack()
# .grid is use to place the items according to a grid 
# Ex:- input.grid(column=0, row=0) (YOU CAN'T USE GRID AND PACK IN THE SAME PROGRAM)

# ______________________________________________________________________________________________________________________

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()        # The cursor starts at that text box (.focus)
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()  # Keep the screen
