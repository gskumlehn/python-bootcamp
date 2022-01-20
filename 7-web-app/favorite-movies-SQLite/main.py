from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# Moviedb API INFO
API_KEY = "YOUR_API_KEY_HERE"
BASE_IMG_URL = "https://www.themoviedb.org/t/p/original"

# Starts app and applies Bootstrap
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)

# Connects to SQLite Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Creates Movie table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.String(4))
    ranking = db.Column(db.Integer)
    review = db.Column(db.Text)
    img_url = db.Column(db.Text, nullable=False)


# Creates Form to search movies titles
class SearchForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    search = SubmitField("Search")


# Creates Form to edit rating and review
class EditForm(FlaskForm):
    rating = StringField("Your rating from 0.0 to 10.0", validators=[DataRequired()])
    review = StringField("Your review", validators=[DataRequired()])
    update = SubmitField("Update")


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
        db.session.commit()

    return render_template("index.html", movies=movies)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(id)
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", id=id, form=form)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        parameters = {
            "api_key": API_KEY,
            "query": form.title.data,
        }
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters)
        results = response.json()['results']

        return render_template("select.html", results=results)

    return render_template("search.html", form=form)


@app.route("/add/<int:movie_id>")
def add(movie_id):
    parameters = {"api_key": API_KEY}
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params=parameters)
    movie_data = response.json()
    new_movie = Movie(title=movie_data['title'],
                      year=movie_data['release_date'][0:4],
                      description=movie_data["overview"],
                      img_url=BASE_IMG_URL + movie_data['backdrop_path'])
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


# Creates DB in case it doesn't exists
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
