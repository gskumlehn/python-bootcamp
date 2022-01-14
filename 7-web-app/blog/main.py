from flask import Flask, render_template, request
import requests
import smtplib

EMAIL = 'YOUR_EMAIL_HERE'
PASSWORD = 'YOUR_PASSWORD_HERE'
post_data = requests.get("https://api.npoint.io/e826bb0d072e441eb66a").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=post_data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:id>')
def post(id):
    requested_post = None
    for post in post_data:
        if post["id"] == id:
            requested_post = post
    return render_template("post.html", id=id, post=requested_post)


def send_email(name, email, phone, message):
    msg = f"Subject:Blog message from {name} \n\n Your received a message in your blog" \
          f"Message:{message}\n\nFrom: {name}\nEmail: {email}\nPhone: {phone}"
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
