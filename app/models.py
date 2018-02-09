from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

# Pitch Model


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """
    Defining the user object
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    # Profile
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    photos = db.relationship('PhotoProfile', backref='user', lazy="dynamic")
    # Blog
    blog = db.relationship('Blog', backref='user', lazy='dynamic')

    # Securing the account
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        """
        Here we take a users password and then hash it.

        We then store the hushed password in password_hash
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Here we compare the hushed password to the users
        password to verify validity
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'

# Profile pictures


class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.String(), primary_key=True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Blog(db.Model):
    """
    Defining the blog object
    """
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    q_body = db.Column(db.String)
    q_author = db.Column(db.String(255))
    p_url = db.Column(db.String())
    category = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    all_blogs = []

    def __init__(self,
                 q_body,
                 q_author,
                 p_url,
                 category,
                 posted):

        self.q_body = q_body
        self.q_author = q_author
        self.p_url = p_url
        self.category = category
        self. posted = posted

    def save_blogs(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
        blogs = Blog.query.all()
        return blogs

    @classmethod
    def get_categories(cls, category):
        blog_cat = Blog.query.filter_by(categor=category)
        return blog_cat
