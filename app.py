import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from forms import AddMoviesForm, AddReviewForm
from sql import new_movie, get_all_movies, get_popular_movies, add_vote, get_movie, get_reviews_for_movie, new_review, \
    delete_movie

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
        db.engine.execute(new_movie, name=form.name.data, description=form.description.data, genre=int(form.genre.data))

        return render_template('home.html')

    return render_template('add_movie.html', form=form)


@app.route('/all', methods=['GET'])
def all_movies():
    query_results = db.engine.execute(get_all_movies)

    return render_template('all_movies.html', query_results=query_results)


@app.route('/popular', methods=['GET'])
def popular_movies():
    query_results = db.engine.execute(get_popular_movies)

    return render_template('popular_movies.html', query_results=query_results)


@app.route('/add_vote/<movie_id>', methods=['POST'])
def add_movie_vote(movie_id):
    template = request.args.get('template')
    db.engine.execute(add_vote, id=int(movie_id))
    query_results = db.engine.execute(get_all_movies) if template == 'all_movies.html' else db.engine.execute(
        get_popular_movies)

    return render_template('{}'.format(template), query_results=query_results)


@app.route('/movie_details/<movie_id>', methods=['GET'])
def movie_details(movie_id):
    movie = db.engine.execute(get_movie, id=movie_id)
    reviews = db.engine.execute(get_reviews_for_movie, id=movie_id)

    return render_template('movie_details.html', movie_query=movie, reviews_query=reviews)


@app.route('/add_review/<movie_id>', methods=['GET', 'POST'])
def add_review(movie_id):
    form = AddReviewForm()

    if form.validate_on_submit():
        db.engine.execute(new_review, movie_id=movie_id, name=form.name.data, review=form.review.data)

        return redirect(url_for('movie_details', movie_id=movie_id))

    return render_template('add_review.html', form=form)


@app.route('/delete_movie/<movie_id>', methods=['POST'])
def remove_movie(movie_id):
    db.engine.execute(delete_movie, id=movie_id)

    return render_template('home.html')


if __name__ == '__main__':
    app.run()
