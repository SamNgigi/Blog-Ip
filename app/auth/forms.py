from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError
from ..models import User


class SignUp(FlaskForm):
    email = StringField('Email', validators=[Required(), Email])
    username = StringField('Your username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo(
        'password2', message='Make sure password match')])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError(
                'Email taken. Check spelling or try another email')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('Username taken. Try another one')


class SignIn(FlaskForm):
    email = StringField('Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
