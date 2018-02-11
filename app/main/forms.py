from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField  # StringField,
from wtforms.validators import Required


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
