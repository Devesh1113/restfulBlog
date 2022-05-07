from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests

TMDB_API_KEY = "6eb03302348c4b9bfc3a483bca77235b"
MOVIE_IMG_URL = "https://image.tmdb.org/t/p/w500"


class RatingForm(FlaskForm):
    text = StringField('Your Rating Out of 10 e.g 7.5', validators=[DataRequired()], name="new_rating")

    review = StringField('Your Review', validators=[DataRequired(), Length(min=10)], name="review")
    submit = SubmitField("Done")


class AddMovies(FlaskForm):
    movie_to_add = StringField('Movie Title', validators=[DataRequired()], name="movie_name")

    submit = SubmitField("Add Movie")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top10movies-collection.db'
db = SQLAlchemy(app)


class MoviesTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<MoviesTable {self.title}>"


db.create_all()


@app.route("/")
def home():
    all_movies = MoviesTable.query.order_by(MoviesTable.rating).all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/<num>", methods=["POST", "GET"])
def edit_rating(num):
    form = RatingForm()
    if request.method == "POST":
        movie_rating = MoviesTable.query.filter_by(id=num).first()
        movie_rating.rating = request.form["new_rating"]
        db.session.commit()

        movie_review = MoviesTable.query.filter_by(id=num).first()
        movie_review.review = request.form["review"]
        db.session.commit()

        return redirect(url_for('home'))

    movie = MoviesTable.query.filter_by(id=num).first()
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete/<num>")
def delete(num):
    movie_to_delete = MoviesTable.query.get(num)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def search_movie():
    new_movie = AddMovies()
    if new_movie.validate_on_submit():
        headers = {
            "api_key": TMDB_API_KEY,
            "query": request.form["movie_name"]
        }

        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=headers)
        data = response.json()
        return render_template("select.html", data=data)

    return render_template("add.html", form=new_movie)


@app.route("/find/<id>")
def add_movie(id):
    headers = {
        "api_key": TMDB_API_KEY
    }
    response2 = requests.get(url=f"https://api.themoviedb.org/3/movie/{id}", params=headers)
    data = response2.json()

    year = data["release_date"].split("-")[0]
    original_title = data["original_title"]
    overview = data["overview"]
    poster_path = data["poster_path"]

    print(year, original_title, overview, poster_path)

    new_movie = MoviesTable(
        title=original_title,
        year=year,
        description=overview,
        img_url=f"{MOVIE_IMG_URL}{poster_path}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
