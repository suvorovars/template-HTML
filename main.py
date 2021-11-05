from os import environ
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('index')
def index():
    return render_template('templates/index.html')

app.run(environ.get('PORT'))