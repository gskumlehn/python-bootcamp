from tkinter import *
from tkinter import messagebox
from pass_gen import pass_gen
from pyperclip import copy
import json


# Imports password generator
def generate():
    entry_pass.delete(0, END)
    password = pass_gen()
    entry_pass.insert(0, password)
    copy(password)


# Saves password
def save():
    website = entry_web.get().capitalize()
    user = entry_user.get()
    password = entry_pass.get()
    new_data = {
        website:
            {'user': user,
             'password': password
             }
    }
    if password == '' or website == '':
        messagebox.showerror(title='Error', message='Data missing')
    else:
        try:
            with open('passwords.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)
        finally:
            with open('passwords.json', 'w') as file:
                json.dump(data, file, indent=4)
            entry_pass.delete(0, END)
            entry_web.delete(0, END)


# Search data
def search():
    website = entry_web.get().capitalize()
    try:
        with open('passwords.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No data file found.')
    else:
        if website in data:
            web_data = data[website]
            user = web_data['user']
            password = web_data['password']
            messagebox.showinfo(title=website, message=f'User: {user}\nPassword: {password}'
                                                       f'\nThe password is already copied (Ctrl+C)')
        else:
            messagebox.showinfo(title=website, message=f'Website "{website}" not found')


# Interface
window = Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')
# Canvas
logo_img = PhotoImage(file='logo.png')
canvas = Canvas(height=200, width=200)
logo = canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# Labels
label_web = Label(text='Website')
label_web.grid(row=1, column=0, sticky="e")
label_user = Label(text='Email/Username')
label_user.grid(row=2, column=0, sticky="e")
label_pass = Label(text='Password')
label_pass.grid(row=3, column=0, sticky="e")
# Entries
entry_web = Entry(width=33)
entry_web.grid(row=1, column=1)
entry_web.focus()
entry_user = Entry(width=48)
entry_user.grid(row=2, column=1, columnspan=2)
entry_user.insert(0, 'gskumlehn@gmail.com')
entry_pass = Entry(width=33)
entry_pass.grid(row=3, column=1)
# Buttons
button_search = Button(text='Search', width=11, command=search)
button_search.grid(row=1, column=2)
button_gen = Button(text="Generate", width=11, command=generate)
button_gen.grid(row=3, column=2, sticky="w")
button_add = Button(text='Add', width=40, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
