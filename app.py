import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import AddMoviesForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.urandom(32)


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
