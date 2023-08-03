# Application package initialization script
# -> Contains the Minimal Application Factory Function

from flask import Flask

# importing all the blueprints
from flaskr.main import bp as main_bp

def create_app():
    """
        application factory function
    """
    app = Flask(__name__)

    # Add configurations here
    # ...
    # ...

    # main blueprint registration
    app.register_blueprint(main_bp)

    return app


