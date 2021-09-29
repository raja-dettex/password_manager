from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_via_website():
    try:
        with open("data.json", "r") as data_read:
            data = json.load(data_read)
        email = data[website_entry.get()]["email"]
        password = data[website_entry.get()]["password"]
        email_entry.insert(0, email)
        password_entry.insert(0, password)
    except KeyError:
        print("data of that particular website does not exist")


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    json_data = {
        website : {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="error", message="fields can not be empty")
    elif len(website) > 0 and len(email) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title=website, message=f"is this the details you entered ! \n Email : {email}"
                                                              f"\n Password : {password} \n is this okay to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(json_data, data_file, indent=4)
            else:
                with open("data.json", "r") as data_file:
                    data.update(json_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()


window.title("password manager")
window.config(padx=20, pady=10)
canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=1)
website_level = Label(text="Website :")
website_level.grid(row=2, column=0)
email_level = Label(text="Email/Username :")
email_level.grid(row=3, column=0)
password_level = Label(text="Password :")
password_level.grid(row=4, column=0)
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=2, column=1)
email_entry = Entry(width=40)
email_entry.grid(row=3, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=4, column=1)
generate_button = Button(text="Generate")
generate_button.grid(row=4, column=2)
search_button = Button(text="search", command=search_via_website)
search_button.grid(row=2, column=2)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
