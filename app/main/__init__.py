from flask import Blueprint

auth = Blueprint('main', __name__)

from . import views, forms, errors
