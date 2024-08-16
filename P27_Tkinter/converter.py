from tkinter import *

def calculation():
    miles = float(input.get())  # Convert input to float for calculation
    km = miles * 1.60934  # Convert miles to kilometers
    value.config(text=f"{km:.2f}")  # Update the 'value' label with the result

window = Tk()
window.title("Mile to Km Converter")    
window.minsize(width=300, height=200)             

# Input field
input = Entry(width=15)
input.grid(column=1, row=0)

# Labels
miles = Label(text="Miles", font=("Arial", 12))
miles.grid(column=2, row=0)

equal = Label(text="is equal to", font=("Arial", 12))
equal.grid(column=0, row=1)

value = Label(text="0", font=("Arial", 12))  # Initial value is set to "0"
value.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 12))
km.grid(column=2, row=1)

# Button
calculate = Button(text="Calculate", command=calculation)
calculate.grid(column=1, row=2)

window.mainloop()
