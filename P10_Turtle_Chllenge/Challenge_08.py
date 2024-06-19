from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height = 400)   # setting screen (width, height)

# Create a prompt
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle win the race?")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]

for turtle_index in range(0,6):
    tim = Turtle(shape = "turtle")      # Change the shape of the arrow to turtle
    tim.penup()
    tim.goto(x = -230, y = y_position[turtle_index])
    tim.color(colors[turtle_index])

screen.exitonclick()