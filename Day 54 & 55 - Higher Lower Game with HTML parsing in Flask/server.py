from flask import Flask
import random

random_number = 0
guessed_number = 0
result = ""

app = Flask(__name__)


@app.route("/")
def guess_number():
    global random_number
    random_number = random.randint(0, 9)
    print(random_number)
    return "<h1>Guess the number between 0 and 9</h1>" \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guessed_number>")
def check_number(guessed_number):
    global result
    if guessed_number < random_number:
        result = f"<h1 style='color:red;'>{guessed_number} is too low</h1>" \
                 "<img src='https://media3.giphy.com/media/c3aZESSDr3vOM/giphy.gif?cid=ecf05e470zz9waou9def3yb3c35l1booyibn94761onbrarm&ep=v1_gifs_related&rid=giphy.gif&ct=g'>"
    elif guessed_number > random_number:
        result = f"<h1 style='color:red;'>{guessed_number} is too high</h1>" \
                 "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guessed_number == random_number:
        result = f"<h1  style='color:green;'>{guessed_number} is correct!!</h1>" \
                 "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    return result


if __name__ == "__main__":
    app.run(debug=True)
