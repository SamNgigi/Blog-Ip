from . import auth
from flask import render_template


@auth.route('/login')
def login():
    auth_test = 'Auth route working!'
    return render_template('auth/login.html', auth_test=auth_test)
