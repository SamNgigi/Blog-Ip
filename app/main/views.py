from . import main
from flask import render_template
# from .. import db


@main.route('/')
def index():
    test = 'Working!'
    return render_template('index.html', test=test)


@main.route('/posts')
def posts():
    test = 'Working'
    return render_template('posts.html', test=test)
