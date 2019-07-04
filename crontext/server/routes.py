
from threading import Lock
import datetime

from flask import render_template, Blueprint, current_app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from crontext.data_packet import TextPacket
from crontext.server.models import db, TextModel


SEND_TIME_LOCK = Lock()  # lock to ensure thread safety when mutating send_time
SEND_TIME = None  # storage for the send time

server = Blueprint("server", __name__)


class TextForm(FlaskForm):
	text_input = StringField("Input Text", validators=[DataRequired()])
	button = SubmitField()


def store_and_create_message(text_input: str) -> TextPacket:
	"""Store the input text message in the database, and return a packet to be
	sent to the worker.
	:param text_input: text message input by user
	"""
	# create the model and store it in the database
	text_model = TextModel(message=text_input, created_at=datetime.datetime.now())
	db.session.add(text_model)
	db.session.commit()

	# construct and return data packet
	return TextPacket(text_input, text_model.id)


@server.route("/", methods=("GET", "POST"))
def index():
	"""Route for the index page of the server application."""
	# get the message channels
	server_to_worker = current_app.extensions["server_to_worker"]
	worker_to_server = current_app.extensions["worker_to_server"]

	form = TextForm()

	if form.validate_on_submit():
		message = store_and_create_message(form.text_input.data)
		server_to_worker.put(message)

	return render_template("base.html", form=form)
