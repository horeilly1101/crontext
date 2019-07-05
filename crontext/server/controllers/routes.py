"""File that contains various routes for the server."""

from flask import render_template, Blueprint, current_app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from crontext.server.controllers.queries import store_and_create_message, update_text_model

server = Blueprint("server", __name__)


class TextForm(FlaskForm):
    """Form that allows the user to input a text message to be sent."""
    text_input = StringField("Input Text", validators=[DataRequired()])
    button = SubmitField()


@server.route("/", methods=("GET", "POST"))
def index():
    """Route for the index page of the server application."""
    # get the message channels
    server_to_worker = current_app.extensions["server_to_worker"]
    worker_to_server = current_app.extensions["worker_to_server"]

    worker_to_server.remove_all_and(update_text_model)

    form = TextForm()

    if form.validate_on_submit():
        message = store_and_create_message(form.text_input.data)
        server_to_worker.put(message)

    return render_template("base.html", form=form)
