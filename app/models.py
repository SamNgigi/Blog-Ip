from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

# Pitch Model


class Users(UserMixin, db.Model):
    """
    Defining the user object
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))


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
    # users_id = db.Column(db.Integer, db.ForeignKey("users.id"))

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
    all_blogs = []
