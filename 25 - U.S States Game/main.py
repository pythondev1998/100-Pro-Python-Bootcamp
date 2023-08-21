import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()

# Buscar por nombre

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50", prompt="What's another state's name? ").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        country = turtle.Turtle()
        country.hideturtle()
        country.penup()
        state_data = data[data.state == answer_state]
        country.goto(int(state_data.x), (int(state_data.y)))
        country.write(state_data.state.item())

screen.exitonclick()
