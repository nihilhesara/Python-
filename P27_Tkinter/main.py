import tkinter

window = tkinter.Tk()
window.title("My first GUI program")    # Window title
window.minsize(width=500,height=300)    # Minimum size of the window 
my_label = tkinter.Label(text="I am a label",font=("Arial",24,"bold"))   # Create the label (It doesn't display)
my_label.pack(side="left")                                 # Setting the label in the window (Default side is center)

window.mainloop()       # Keep the screen 