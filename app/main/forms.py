from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, RadioField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Required
from .. import photos


class BlogForm(FlaskForm):
    p_body = TextAreaField('Description', validators=[Required()])
    p_author = StringField('Username', validators=[Required()])
    category = RadioField('Pick Category',
                          choices=[('people', 'people'),
                                   ('nature', 'nature'),
                                   ('artchitecture', 'artchitecture')],
                          validators=[Required()])
    p_url = FileField('Upload photo', validators=[
                      FileRequired(), FileAllowed(photos, 'Images only.')])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
