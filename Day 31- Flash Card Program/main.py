from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"

# -------------------------Read from csv---------------------#
file_data = pandas.read_csv("/Users/marin/PycharmProjects/Day 31- Flash Card Program/data/french_words.csv")
know_list = []
random_row = None
new_data = {}

# -------------------------Create UI -------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=600)
canvas.grid(column=1, row=1)

front_card_filename = PhotoImage(
    file="/Users/marin/PycharmProjects/Day 31- Flash Card Program/images/card_front.png")

back_card_filename = PhotoImage(file="/Users/marin/PycharmProjects/Day 31- Flash Card Program/images/card_back.png")
display_word = Label(text="", font=("Courier", 50, "bold"), bg="white")

front_card = canvas.create_image(400, 260, image=front_card_filename)


def read_file():
    try:
        with open(file="data/words to learn.txt", mode="r") as file:
            know_list = file.readlines()

    except FileNotFoundError:
        with open(file="data/words to learn.txt", mode="w") as file:
            file.write("")
    else:
        random_word = random.choice(file_data["French"])
        print(know_list)
        while random_word in know_list:
            print("word found in the file")
            random_word = random.choice(file_data["French"])
        return file_data[file_data["French"] == random_word]


def new_card():
    global random_row
    random_row = read_file()
    canvas.itemconfig(front_card, image=front_card_filename)
    display_word.config(text=f"French word:\n\n{random_row['French'].item()}", font=("Courier", 50, "bold"),
                        bg="white")

    display_word.place(x=150, y=150)
    window.after(3000, func=flip_card)


def flip_card():
    global random_row
    canvas.itemconfig(front_card, image=back_card_filename)
    display_word.config(text=f"English word:\n\n{random_row['English'].item()}", font=("Courier", 50, "bold"),
                        bg="#91C2AF")


def add_to_know_list():
    global random_row, know_list
    new_data = f"{random_row['French'].item()}, {random_row['English'].item()}\n"
    print(new_data)
    with open(file="data/words to learn.txt", mode="a") as file:
        file.write(new_data)

    new_card()


wrong_image_filename = PhotoImage(file="/Users/marin/PycharmProjects/Day 31- Flash Card Program/images/wrong.png")
wrong_button = Button(image=wrong_image_filename, highlightthickness=0, bg=BACKGROUND_COLOR, border=0,
                      command=new_card)
wrong_button.place(x=100, y=525)

right_image_filename = PhotoImage(file="/Users/marin/PycharmProjects/Day 31- Flash Card Program/images/right.png")
right_button = Button(image=right_image_filename, highlightthickness=0, bg=BACKGROUND_COLOR, border=0,
                      command=add_to_know_list)
right_button.place(x=600, y=525)

new_card()

window.mainloop()
