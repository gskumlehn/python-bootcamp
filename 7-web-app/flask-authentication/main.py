from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Initializes flask and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initializes the login manager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Creates table in database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Homepage
@app.route('/')
def home():
    return render_template("index.html")


# Registry page
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks if email already signed up
        if User.query.filter_by(email=request.form.get('email')).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        # Creates new user with hashed and salted password and adds to database
        new_user = User(email=request.form.get("email"),
                        name=request.form.get("name"),
                        password=generate_password_hash(request.form.get("password"), "pbkdf2:sha256", 8))
        db.session.add(new_user)
        db.session.commit()
        # Logs user in
        login_user(new_user)

        return redirect(url_for("secrets"))

    return render_template("register.html")


# Login Page
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # Gets user from database by email
        user = User.query.filter_by(email=email).first()

        # Check if email is already signed up
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Checks if password matches hashed and salted password in database
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        # Logs user in
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html")


# Secrets Page
@app.route('/secrets')
# Requires authentication to render page
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


# Logs user out
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


# Opens file to browser
@app.route('/download')
@login_required
def download():
    return send_from_directory("static", filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run()
