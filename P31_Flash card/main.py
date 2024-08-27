from tkinter import *
import os
import pandas
import random

# Set the background color
BACKGROUND_COLOR = "#B1DDC6"

# Change the current working directory to the directory where the script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize variables to store the current card and the list of cards to learn
current_card = {}
to_learn = {}

# Try to load the saved list of words to learn from a CSV file
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # If the file is not found, load the original list of French words
    original_data = pandas.read_csv("data/french_word.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # If the file is found, use the loaded data
    to_learn = data.to_dict(orient="records")

def next_card():
    """Selects a random card and displays it on the front side of the flashcard."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel any existing timer for flipping the card
    current_card = random.choice(to_learn)  # Choose a random card from the list
    canvas.itemconfig(card_title, text="French", fill="black")  # Set the title to "French" with black text
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")  # Display the French word in black
    canvas.itemconfig(card_background, image=card_front_image)  # Show the front image of the card
    flip_timer = window.after(3000, func=flip_card)  # Set a timer to flip the card after 3 seconds

def flip_card():
    """Flips the flashcard to show the English translation on the back side."""
    canvas.itemconfig(card_title, text="English", fill="White")  # Set the title to "English" with white text
    canvas.itemconfig(card_word, text=current_card["English"], fill="White")  # Display the English word in white
    canvas.itemconfig(card_background, image=card_back_image)  # Show the back image of the card

def is_known():
    """Removes the current card from the list of words to learn and updates the file."""
    to_learn.remove(current_card)  # Remove the current card from the list
    data = pandas.DataFrame(to_learn)  # Convert the updated list to a DataFrame
    data.to_csv("data/words_to_learn.csv", index=False)  # Save the updated list to a CSV file
    next_card()  # Move to the next card

# Set up the main window
window = Tk()
window.title("Flash card")  # Set the window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Set padding and background color

# Set a timer to flip the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Create a canvas to hold the flashcard images and text
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")  # Load the front image of the flashcard
card_back_image = PhotoImage(file="images/card_back.png")  # Load the back image of the flashcard
card_background = canvas.create_image(400, 263, image=card_front_image)  # Set the initial image to the front
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # Set background color and remove border
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))  # Create the title text
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))  # Create the word text
canvas.grid(column=0, row=0, columnspan=2)  # Place the canvas on the grid

# Create the "wrong" button (cross image) to move to the next card
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)  # Clicking it calls next_card()
unknown_button.grid(column=0, row=1)  # Place the button on the grid

# Create the "right" button (check image) to mark the card as known
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=is_known)  # Clicking it calls is_known()
known_button.grid(column=1, row=1)  # Place the button on the grid

# Display the first card when the program starts
next_card()

# Start the main event loop to keep the window open
window.mainloop()
