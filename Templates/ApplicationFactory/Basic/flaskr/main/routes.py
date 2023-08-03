# routes main blueprint

from flask import (
    render_template
)

from flaskr.main import bp

@bp.route("/", methods=["GET"])
def index():
    """
        view function for home page
    """

    # data dictionary which is passed to the template
    # to render data on the frontend
    data={}

    data["title"] = "HOME"

    return render_template("main/index.html",data=data)
