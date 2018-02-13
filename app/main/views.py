from . import main
from flask import render_template, redirect, url_for  # , request
from ..models import Blog, Comments
from .forms import CommentForm, BlogForm
from flask_login import login_required, current_user
from .. import db  # , photos


@main.route('/')
def index():
    test = 'Working!'
    return render_template('index.html', test=test)


@main.route('/gallery')
def gallery():
    all = Blog.query.all()
    people = Blog.query.filter_by(category='people').all()
    nature = Blog.query.filter_by(category='nature').all()
    architecture = Blog.query.filter_by(category='architecture').all()
    test = 'Working'
    return render_template('gallery.html',
                           all=all,
                           test=test,
                           nature=nature,
                           people=people, architecture=architecture)


@main.route('/blog', methods=['GET', 'POST'])
def blog():
    test = 'What does minimalism mean for you?'
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        p_body = blog_form.p_body.data
        p_author = blog_form.p_author.data
        category = blog_form.category.data
        p_url = blog_form.p_url.data
        new_post = Blog(p_body=p_body,
                        p_author=p_author,
                        category=category,
                        p_url=p_url)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.blog'))
    return render_template('blog.html', test=test, blog_form=blog_form)


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
