from flask import render_template, Blueprint

from crontext.message import Message
from crontext.server import _app, TextForm, _server_to_text
from threading import Lock

SEND_TIME_LOCK = Lock()  # lock to ensure thread safety when mutating send_time
SEND_TIME = None  # storage for the send time

server = Blueprint("server", __name__)


@server.route("/", methods=("GET", "POST"))
def index():
	"""Route for the index page of the server application."""
	form = TextForm()

	if form.validate_on_submit():
		_server_to_text.put("{}".format(Message(form.text_input.data)))

	return render_template("base.html", form=form)
