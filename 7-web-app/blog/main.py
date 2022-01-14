from flask import Flask, render_template
import requests

post_data = requests.get("https://api.npoint.io/e826bb0d072e441eb66a").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=post_data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def post(id):
    requested_post = None
    for post in post_data:
        if post["id"] == id:
            requested_post = post

    return render_template("post.html", id=id, post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
