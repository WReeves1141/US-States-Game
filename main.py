# ========================================================================== #
# Programmer : Walter Reeves
#
# Description:
#   This program plays a fifty state guessing game.
#
# Enhancement:
#   Add game over message.
#   Fix alignment of the state names.
#   Change location of text input box on screen.
# ========================================================================== #
import turtle
import pandas

# Initializes the background.
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Global Lists
guessed_states = []

while len(guessed_states) < 50:
    # Prompts for a state name.
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/50", \
                                    prompt="What's another state's name?",)
    answer_state = answer_state.title()

    # Adds all the state names to a list.
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.to_list()

    if answer_state in state_list:
        guessed_states.append(answer_state)

        # Writes the state name on the state.
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        tim.write(answer_state)

screen.exitonclick()
