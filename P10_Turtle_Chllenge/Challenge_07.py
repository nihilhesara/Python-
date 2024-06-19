from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    new_heading = tim.heading() + 10        # Turn left by 10 degrees 
    tim.setheading(new_heading)

def move_right():
    new_heading = tim.heading() - 10        # Turn right by 10 degrees 
    tim.setheading(new_heading)

def clear():
    tim.clear()     # Clear the entier screen
    tim.penup()
    tim.home()      # Geth the cursor to the middle of the page 
    tim.pendown()

# Python event listners
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()