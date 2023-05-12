# Importing necessary libraries.
import turtle
import pandas
from state import State

# Creating a Turtle Screen and setting title.
screen = turtle.Screen()
screen.title("U.S. States Game")

# Adding the image of the blank U.S. map to the screen.
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Initialising variables.
score = 0
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
correct_guesses = []

# Starting the game loop.
while score < 50:
    # Getting the user's answer through a text input box.
    user_answer = screen.textinput(title=f"{score}/50 States correct", prompt="Enter a State: ").title()
    
    # Checking if the user wants to give up.
    if user_answer == "Give Up":
        break
        
    # Checking if the answer has already been guessed correctly.
    if user_answer not in correct_guesses:
        # Checking if the answer is a valid state.
        if user_answer in states_list:
            # Adding the answer to the list of correct guesses.
            correct_guesses.append(user_answer)
            # Increasing the score by 1.
            score += 1
            # Getting the row of the guessed state from the data DataFrame.
            state_row = data[data.state == user_answer]
            # Getting the x and y coordinates of the guessed state.
            x_cor = float(state_row.x)
            y_cor = float(state_row.y)
            # Creating a State turtle object at the guessed state's coordinates.
            write_state = State()
            write_state.goto(x_cor, y_cor)
            # Writing the guessed state's name on the map.
            write_state.write(user_answer, align="center", font=("arial", 9, "normal"))

# Turning off the screen's tracer to speed up the rendering.
screen.tracer(0)

# Creating a list of states that were not guessed correctly.
not_guessed = [state for state in states_list if state not in correct_guesses]

# Looping over the list of not guessed states and marking them on the map in red.
for state in not_guessed:
    state_row = data[data.state == state]
    x_cor = float(state_row.x)
    y_cor = float(state_row.y)
    write_state = State()
    write_state.color("red")
    write_state.goto(x_cor, y_cor)
    write_state.write(state, align="center", font=("arial", 9, "normal"))

# Updating the screen to render the changes made to the map.
screen.update()

# Creating a DataFrame of not guessed states and saving it to a CSV file.
not_guessed_df = pandas.DataFrame(not_guessed)
not_guessed_df.to_csv("states_not_guessed.csv")

# Exiting the screen when the user clicks on it.
screen.exitonclick()