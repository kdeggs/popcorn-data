import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
