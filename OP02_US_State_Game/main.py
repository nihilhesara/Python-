import turtle
import os
import pandas

# Change directory to the location of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

'''def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()                               # To continue the screen if user click the screen
# User can run the above code and click the state and then the x and y value will print in the console 
# _____________________________________________________________________________________________________'''
guessed_states = []

while len(guessed_states) <50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title() # Convert 1st letter to capital
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())    # Capturing single element using .item
        t.write(answer_state)

screen.exitonclick()

#turtle.mainloop()                               # To continue the screen if user click the screen

# states to learn.csv