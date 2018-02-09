from . import auth
from .. import db
from ..models import User
from .forms import SignUp, SignIn
from flask_login import login_required
from flask import render_template, redirect, url_for, flash


@auth.route('/register')
def register():
    register_test = 'Sign Up route working!'
    sign_up = SignUp()
    if sign_up.validate_on_submit():
        user = User(email=sign_up.email.data,
                    username=sign_up.username.data,
                    password=sign_up.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html',
                           register_test=register_test,
                           sign_up=sign_up)


@auth.route('/login')
def login():
    login_test = 'Sign In route working!'
    sign_in = SignIn()
    return render_template('auth/login.html',
                           login_test=login_test,
                           sign_in=sign_in)


@auth.route('/logout')
@login_required
def logout():
    logout_test = 'Log out working!'
    flash('You have been successfully logged out')
    return redirect(url_for('main.index'), logout_test=logout_test)
