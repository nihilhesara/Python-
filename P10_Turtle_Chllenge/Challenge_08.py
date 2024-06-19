from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width = 500, height = 400)   # setting screen (width, height)

# Create a prompt
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle win the race?")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle")      # Change the shape of the arrow to turtle
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()