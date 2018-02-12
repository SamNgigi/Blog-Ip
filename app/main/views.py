from . import main
from flask import render_template, redirect, url_for, request
from ..models import Blog, Comments
from .forms import CommentForm
from flask_login import login_required, current_user
from .. import db, photos


@main.route('/')
def index():
    test = 'Working!'
    return render_template('index.html', test=test)


@main.route('/gallery')
def gallery():
    architecture = Blog.query.filter_by(category='architecture').all()
    test = 'Working'
    return render_template('gallery.html',
                           test=test, architecture=architecture)


@main.route('/blog', methods=['GET', 'POST'])
def blog():
    test = 'What does minimalism mean for you?'
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename
    return render_template('blog.html', test=test)


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


@main.route('/delete/<int:id>')
@login_required
def delete(id):
    del_comment = Comments.query.get(id)
    db.session.delete(del_comment)
    db.session.commit()
    return redirect(url_for('main.gallery'))
