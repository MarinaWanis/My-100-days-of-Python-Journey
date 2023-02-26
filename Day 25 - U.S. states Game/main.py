from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
state_writer = Turtle()

state_writer.penup()
state_writer.hideturtle()

image = "blank_states_img.gif"
data_csv = "50_states.csv"
score = 0
total_states = 50
FONT = ("Courier", 8, "normal")
user_guesses = []

states_to_learn = {"States": []}

while len(user_guesses) < 50:
    screen.addshape(image)
    turtle.shape(image)

    user_input = screen.textinput(f"Correct Guesses: {score}/{total_states}", "What's the state you guess?").title()

    if user_input == "Exit":
         break

    all_states = pandas.read_csv(data_csv)
    state_row = all_states[all_states["state"] == user_input]

    if user_input in all_states.values:
        if user_input not in user_guesses:
            user_guesses.append(user_input)
            score += 1
            state_writer.goto(float(state_row["x"]), float(state_row["y"]))
            state_writer.write(user_input, align="center", font=FONT)
        # print(user_guesses)



screen.exitonclick()

all_states = pandas.read_csv(data_csv)


print(type(all_states.state.values))
#
# for state in all_states.state.values:
#     if state not in user_guesses:
#         states_to_learn["States"].append(state)

states_to_learn = [state for state in all_states.state.values if state not in user_guesses]
print(states_to_learn)

# print(states_to_learn)
df = pandas.DataFrame(states_to_learn)
df.to_csv("States To Learn.csv")


