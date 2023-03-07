from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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
    empty_password = len(password)

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if empty_website == 0 or empty_password == 0:
        messagebox.showwarning(title="Unable to save credentials", message="Website/Password field is empty")

    else:
        is_ok = messagebox.askokcancel(title="Confirm",
                                       message=f"Are you sure you want to save the following?:\n \nWebsite: {website}\n\n"
                                               f"Username/email: {email}\n\nPassword: {password}")

        if is_ok:
            try:
                with open("My credentials.json", mode="r") as file:
                    current_data = json.load(file)

            except FileNotFoundError:
                with open("My credentials.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating the data
                current_data.update(new_data)

                with open("My credentials.json", mode="w") as file:
                    # Writing the new data to the file
                    json.dump(current_data, file, indent=4)
            finally:
                website_text.delete("1.0", END)
                password_text.delete("1.0", END)


# -----------------------------Search Website -------------------------#

def search():
    search_website = website_text.get("1.0", END).strip()
    try:
        with open("My credentials.json") as file:
            data = json.load(file)
            messagebox.showinfo(title=f"{search_website}",
                                message=f"Email: {data[f'{search_website}']['email']}\n\nPassword: "
                                        f"{data[f'{search_website}']['password']}")
            print(data["test2"])
    except FileNotFoundError:
        messagebox.showwarning(title="Unable to Search", message="File doesn't exist, you need to add credentials first")
    except KeyError:
        if search_website == "":
            messagebox.showwarning(title="Unable to Search", message="Website is blank")
        else:
            messagebox.showwarning(title="Website not found", message=f"Website: {search_website} is not found in the "
                                                                  f"credentials file")




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

website_text = Text(width=26, height=1, bg="white")
website_text.grid(column=1, row=2)
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

generate_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_button.grid(column=2, row=4)

add_button = Button(text="Add", bg="white", width=45, command=add_credentials)
add_button.grid(column=1, row=5, columnspan=2)

search_button = Button(width=15, text="Search", bg="white", command=search)
search_button.grid(column=2, row=2)

window.mainloop()
