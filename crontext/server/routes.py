from flask import render_template

from crontext.message import Message
from crontext.server import _app, TextForm, server_to_text
from threading import Lock

SEND_TIME_LOCK = Lock()  # lock to ensure thread safety when mutating send_time
SEND_TIME = None  # storage for the send time


@_app.route("/", methods=("GET", "POST"))
def index():
	"""Route for the index page of the server application."""
	form = TextForm()

	if form.validate_on_submit():
		server_to_text.put("{}".format(Message(form.text_input.data)))

	return render_template("base.html", form=form)
