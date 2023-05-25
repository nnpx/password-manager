from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if website_data == "" or email_data == "" or password_data == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered: \nEmail: {email_data}"
                                                           f"\nPassword: {password_data} \nIs it the data above correct?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)

            finally:
                website_input.delete(0, "end")
                password_input.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:")
website_text.grid(column=0, row=1)
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)

email_text = Label(text="Email/ Username:")
email_text.grid(column=0, row=2)
email_input = Entry(width=39)
email_input.grid(column=1, columnspan=2, row=2)
email_input.insert(END, "randomgmail@gmail.com")

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, columnspan=2, row=4)




window.mainloop()