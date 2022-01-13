from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

# Opens csv file to DataFrame and transforns into dictionary
df = pd.read_csv('data/french_words.csv')
french_english = df.to_dict(orient='records')
pair = choice(french_english)

# Fetches next card
def next_card():
    global pair, timer
    window.after_cancel(timer)
    pair = choice(french_english)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word, text=pair['French'], fill='black')
    canvas.itemconfig(card, image=card_front)
    timer = window.after(3000, func=turn)

# Removes learned words from csv file
def learned():
    global pair, french_english
    french_english.remove(pair)
    with open('words_to_learn.csv', 'w') as file:
        new_df = pd.DataFrame(french_english)
        new_df.to_csv(file, index=False)
    next_card()

# Turns from french to english
def turn():
    global pair
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=pair['English'], fill='white')
    canvas.itemconfig(card, image=card_back)

# Window
window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
timer = window.after(30000, func=turn)
# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# Image
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card =canvas.create_image(400, 263, image=card_front)
# Text
language = canvas.create_text(400, 180, text='Language', font=('Arial', 30, 'italic'))
word = canvas.create_text(400, 270, text='word', font=('TimeNewRoman', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)
# Buttons
right = PhotoImage(file='images/right.png')
right_button = Button(image=right, bg=BACKGROUND_COLOR, highlightthickness=0, command=learned)
right_button.grid(row=1, column=0)

wrong = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

window.mainloop()

