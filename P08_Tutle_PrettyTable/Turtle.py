from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")   # To change the shape of the cursor 
timmy.color("red")      # To change the color of the cursor
timmy.forward(100)      # To get the cursor 100px forward

my_screen = Screen()    # To display the screen
print(my_screen.canvheight)
my_screen.exitonclick() # To exit the screen on a click

# https://pypi.org/ use to find packages in python
# turtle document https://docs.python.org/3/library/turtle.html