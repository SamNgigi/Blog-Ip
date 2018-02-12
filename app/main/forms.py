from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, RadioField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    p_body = TextAreaField('Description', validators=[Required()])
    p_author = StringField('Username', validators=[Required()])
    category = RadioField('Pick Category',
                          choices=[('people', 'people'),
                                   ('nature', 'nature'),
                                   ('artchitecture', 'artchitecture')],
                          validators=[Required()])
    p_url = TextAreaField('Enter image url', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
