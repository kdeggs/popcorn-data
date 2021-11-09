import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
from forms import AddMoviesForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
db = SQLAlchemy(app)


class Genre(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(), nullable=False)


class Movies(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    genre = db.Column(db.Integer, db.ForeignKey('genre.genre_id'), nullable=False)
    votes = db.Column(db.Integer, default=0, nullable=False)


class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False)
    reviewer_name = db.Column(db.String, nullable=False)
    review = db.Column(db.String, nullable=False)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/all', methods=['GET', 'POST'])
def allMovies():
    return render_template('allmovies.html')


@app.route('/add', methods=['GET', 'POST'])
def addMovie():
    form = AddMoviesForm()
    return render_template('addmovie.html', form=form)


if __name__ == '__main__':
    app.run()
