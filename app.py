import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from forms import AddMoviesForm
from sql import new_movie, get_all_movies

load_dotenv()

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


@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    form = AddMoviesForm()

    if form.validate_on_submit():
        db.engine.execute(
            new_movie,
            name=form.name.data,
            description=form.description.data,
            genre=int(form.genre.data)
        )

        return render_template('home.html')

    return render_template('add_movie.html', form=form)


@app.route('/all', methods=['GET'])
def all_movies():
    query_results = db.engine.execute(get_all_movies)

    return render_template('all_movies.html', query_results=query_results)


if __name__ == '__main__':
    app.run()
