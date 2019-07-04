from flask import render_template, Blueprint, current_app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from crontext.message import Message
from threading import Lock

SEND_TIME_LOCK = Lock()  # lock to ensure thread safety when mutating send_time
SEND_TIME = None  # storage for the send time

server = Blueprint("server", __name__)


class TextForm(FlaskForm):
	text_input = StringField("Input Text", validators=[DataRequired()])
	button = SubmitField()


@server.route("/", methods=("GET", "POST"))
def index():
	"""Route for the index page of the server application."""
	form = TextForm()

	if form.validate_on_submit():
		current_app.extensions["server_to_worker"].put("{}".format(Message(form.text_input.data)))

	return render_template("base.html", form=form)
