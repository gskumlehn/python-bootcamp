from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

#  Creates app and applies Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = "3290fsjdj4r32hfwoe"
Bootstrap(app)

# Creates a database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Creates Table in database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(250), nullable=False)


# Creates WTForm for adding books
class BookForm(FlaskForm):
    title = StringField("Book Title", validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = SelectField("Rating", choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    add = SubmitField("Add Book")


#  Creates a WTForm to edit book rating
class EditForm(FlaskForm):
    rating = SelectField("Rating", choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    edit = SubmitField("Change Rating")


# Apply the creation of database and table
db.create_all()


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        # Creates a new row in table
        new_book = Book(title=form.title.data, author=form.author.data, rating=form.rating.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    if form.validate_on_submit():
        # Updates rating of book by id
        book_to_update = Book.query.get(id)
        book_to_update.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    book = Book.query.get(id)
    return render_template("edit.html", form=form, book=book)


@app.route("/delete/<int:id>")
def delete(id):
    # Deletes a row by id
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
