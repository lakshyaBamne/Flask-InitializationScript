# main blueprint which serves the home page for the application

from flask import Blueprint

bp = Blueprint('main', __name__)

from flaskr.main import routes