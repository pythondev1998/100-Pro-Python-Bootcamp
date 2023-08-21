from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    """
    Is the same :D
    for char in password_list:
      password += char
    """
    pyperclip.copy(password)
    input_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    email = input_email_username.get()
    password = input_password.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning("Oops", "Please don't leave any fields empty! ")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)  # Mode r
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_password():
    website = input_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ", bg="white")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username: ", bg="white")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0)

# Inputs
input_website = Entry(width=21)
input_website.grid(row=1, column=1)
input_website.focus()

input_email_username = Entry(width=35)
input_email_username.grid(row=2, column=1, columnspan=2)
input_email_username.insert(0, "brian@email.com")

input_password = Entry(width=21)
input_password.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", highlightthickness=0, width=16, command=find_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate password", highlightthickness=0, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightthickness=0, width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
