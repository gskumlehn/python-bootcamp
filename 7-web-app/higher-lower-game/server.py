from flask import Flask
from random import randint

app = Flask(__name__)
NUMBER = randint(0,100)

# Starts game
@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 100</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

# Depending on the number you chose, renders different images and messages
@app.route("/<int:number>")
def number(number):
    global NUMBER

    if NUMBER == number:
        return "<h1 style='color: lightgreen'>RIGHT ON BROTHER</h1>" \
               "<img src= 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif NUMBER < number:
        return "<h1 style='color: red'>TOO HIGH, try again</h1>" \
               "<img src= 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif NUMBER > number:
        return "<h1 style='color: blue'>TOO LOW, try again</h1>" \
               "<img src= 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"



if __name__ == "__main__":
    app.run(debug=True)