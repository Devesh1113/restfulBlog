from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
import sqlite3
from sqlite3 import Error


# def create_connection(db_file):
#     """ create a database connection to a SQLite database """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()
#
#
# if __name__ == '__main__':
#     create_connection(r"C:\DEVESH\password_manager.db")

# connection object
connection_obj = sqlite3.connect('password.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# Creating table
table = """ CREATE TABLE GEEK (
            Company CHAR(255) NOT NULL,
            Email VARCHAR(255) NOT NULL,
            Password CHAR(255) NOT NULL
        ); """

cursor_obj.execute(table)




# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    web_text = web_entry.get()
    email_text = email_entry.get()
    pass_text = pass_entry.get()
    cursor_obj.execute("INSERT INTO GEEK VALUES (?, ?, ?);", (web_text, email_text, pass_text))
    connection_obj.commit()

    if len(web_text) == 0 or len(pass_text) == 0:
        messagebox.showwarning(title="Waring", message="Please fill the empty fields!")


def find_password():
    website = web_entry.get()

    conn = sqlite3.connect('password.db')

    statement = '''SELECT * FROM GEEK'''

    cursor_obj.execute(statement)

    row = cursor_obj.fetchall()
    print(row)
    conn.commit()

    # if row[0] == website:
    #     print(row[0])
    #     pyperclip.copy(row[2])
    #     messagebox.showinfo(title=website.title(), message=f"Email: {row[1]}\nPassword: {row[2]} ")
    # else:
    #     messagebox.showwarning(title="Error", message="No Data File Found")

    # try:
    #     read = json.load(data_file)
    # except FileNotFoundError:
    #     messagebox.showwarning(title="Error", message="No Data File Found")
    # if website in read:
    #     my_password = read[website]["password"]
    #     pyperclip.copy(my_password)
    #     messagebox.showinfo(title=website.title(), message=f"Email: {email_entry.get()}\nPassword: {my_password} ")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email / Username")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password")
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, sticky=EW)

email_entry = Entry(width=35)
email_entry.insert(END, string="deveshk237@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, sticky=EW)

# Buttons
pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(row=3, column=2, sticky=EW)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky=EW)

window.mainloop()
