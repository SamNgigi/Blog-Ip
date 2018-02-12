from . import auth
from .. import db
from ..models import User
from .forms import SignUp, SignIn
from flask_login import login_required, login_user
from flask import render_template, redirect, request, url_for, flash


@auth.route('/register', methods=["GET", "POST"])
def register():
    sign_up = SignUp()

    if sign_up.validate_on_submit():
        user = User(email=sign_up.email.data,
                    username=sign_up.username.data,
                    password=sign_up.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html',
                           sign_up=sign_up,
                           title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_test = 'Sign In route working!'
    sign_in = SignIn()
    if sign_in.validate_on_submit():
        user = User.query.filter_by(email=sign_in.email.data).first()
        if user is not None and user.verify_password(sign_in.password.data):
            login_user(user, sign_in.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

    return render_template('auth/login.html',
                           login_test=login_test,
                           sign_in=sign_in)


@auth.route('/logout')
@login_required
def logout():
    flash('You have been successfully logged out')
    return redirect(url_for('main.index'))
