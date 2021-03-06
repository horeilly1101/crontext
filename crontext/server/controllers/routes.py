"""File that contains various routes for the server."""

from flask import render_template, Blueprint, current_app
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

from crontext.server.controllers.queries import store_and_create_message, update_text_model, get_text_list

server = Blueprint("server", __name__)


class TextForm(FlaskForm):
    """Form that allows the user to input a text message to be sent."""
    text_input = TextAreaField("Input Text", validators=[DataRequired()])
    button = SubmitField()


@server.route("/", methods=("GET", "POST"))
def index():
    """Route for the index page of the server application."""
    # get the broker
    broker = current_app.extensions["broker"]

    # receive and handle packets from the worker
    broker.remove_all_and(update_text_model)

    form = TextForm()

    if form.validate_on_submit():
        # store and then send text messages to the worker
        message = store_and_create_message(form.text_input.data)
        broker.put(message)

    texts = get_text_list()
    return render_template("base.html", form=form, texts=texts)
