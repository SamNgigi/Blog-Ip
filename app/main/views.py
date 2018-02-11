from . import main
from flask import render_template, redirect, url_for
from ..models import Blog, Comments
from .forms import CommentForm
from flask_login import login_required, current_user
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
@login_required
def comments(id):
    comment_form = CommentForm()
    comments = Comments.query.order_by('-id').limit(3).all()
    blog = Blog.query.get(id)
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        # category=category
        new_comment = Comments(comment=comment,
                               users=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('main.comments', id=blog.id))
    return render_template('comments.html',
                           blog=blog,
                           comments=comments,
                           comment_form=comment_form)
