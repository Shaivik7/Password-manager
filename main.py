import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- Search Website ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("Saved Info.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"No records of {website}")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n "
                                                           f"Password: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No records of {website}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range (nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range (nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range (nr_symbols)]

    password_list = password_symbols + password_numbers + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_dict = {
        website: {
            "email": email,
            "password": password,

    }}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("Saved Info.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("Saved Info.json", "w") as file:
                json.dump(new_dict, file, indent=4)
        else:
            data.update(new_dict)
            with open("Saved Info.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
project = tkinter
window = project.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Create Image
canvas = project.Canvas(height=200, width=200)
logo_img = project.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = project.Label(text="Website :")
website_label.grid(row=1, column=0)

email_label = project.Label(text="Email/Username :")
email_label.grid(row=2, column=0)

password_label = project.Label(text="Password :")
password_label.grid(row=3, column=0)

# Entries
website_entry = project.Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = project.Entry(width=35)
email_entry.grid(row=2, column=1)

password_entry = project.Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = project.Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = project.Button(text="Add", width=50,command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = project.Button(text="Search", command=find_password,width=14)
search_button.grid(row=1, column=2)

window.mainloop()
