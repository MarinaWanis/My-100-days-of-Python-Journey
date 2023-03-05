from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_range = random.randint(8, 10)
    number_range = random.randint(2, 4)
    symbols_range = random.randint(2, 4)

    random_letters = [letters[random.randint(0, 51)] for letter in range(0, letter_range)]
    random_numbers = [numbers[random.randint(0, 9)] for number in range(0, number_range)]
    random_symbols = [symbols[random.randint(0, 8)] for symbol in range(0, symbols_range)]
    random_password = random_letters + random_numbers + random_symbols
    random.shuffle(random_password)

    final_password = ''.join(random_password)
    password_text.delete("1.0", END)
    password_text.insert(END, final_password)
    pyperclip.copy(final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_credentials():
    website = website_text.get('1.0', END).strip()
    email = email_text.get('1.0', END).strip()
    password = password_text.get('1.0', END).strip()
    text = f"{website} | {email} | {password} \n"

    empty_website = len(website)
    empty_email = len(email)
    empty_password = len(password)

    if empty_website == 0:
        messagebox.showwarning(title="Unable to save credentials", message="Website field is empty")
    elif empty_email == 0:
        messagebox.showwarning(title="Unable to save credentials", message="Username/email field is empty")
    elif empty_password == 0:
        messagebox.showwarning(title="Unable to save credentials", message="Password field is empty")
    else:
        is_ok = messagebox.askokcancel(title="Confirm",
                                       message=f"Are you sure you want to save the following?:\n \nWebsite: {website}\n\n"
                                               f"Username/email: {email}\n\nPassword: {password}")

        if is_ok:
            with open("My credentials.txt", mode="a") as file:
                file.write(text)
            website_text.delete("1.0", END)
            password_text.delete("1.0", END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=40, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)

logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=1)

website_title = Label(text="Website:", bg="white")
website_title.grid(column=0, row=2)

website_text = Text(width=40, height=1, bg="white")
website_text.grid(column=1, row=2, columnspan=2)
website_text.focus()
website = website_text.get('1.0', 'end')

email_title = Label(text="Email/Username:", bg="white")
email_title.grid(column=0, row=3)

email_text = Text(width=40, height=1, bg="white")
email_text.grid(column=1, row=3, columnspan=2)
email_text.insert(END, "marinamaged1996@outlook.com")

password_title = Label(text="Password:", bg="white")
password_title.grid(column=0, row=4)

password_text = Text(width=26, height=1, bg="white")
password_text.grid(column=1, row=4)

generate_button = Button(text="Genertae Password", bg="white", command=generate_password)
generate_button.grid(column=2, row=4)

add_button = Button(text="Add", bg="white", width=45, command=add_credentials)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
