import turtle
import os

# Change directory to the location of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()                               # To continue the screen if user click the screen

# User can run the above code and click the state and then the x and y value will print in the console 
# _____________________________________________________________________________________________________