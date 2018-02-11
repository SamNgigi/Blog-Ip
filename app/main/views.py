from . import main
from flask import render_template
from ..models import Blog
# from .. import db


@main.route('/')
def index():
    test = 'Working!'
    return render_template('index.html', test=test)


@main.route('/posts')
def posts():
    architecture = Blog.query.filter_by(category='architecture').all()
    test = 'Working'
    return render_template('posts.html', test=test, architecture=architecture)


@main.route('/comments/<int:id>', methods=['GET', 'POST'])
def comments(id):
    test = "Working!"
    blog = Blog.query.get(id)
    return render_template('comments.html', test=test, blog=blog)
