"""defines the structure of the main app"""

import logging
from threading import Thread

from flask_wtf import FlaskForm
from wtforms import StringField
from flask import Flask, render_template
from wtforms.validators import DataRequired

from crontext.message import Message
from crontext.safe_queue import SafeQueue

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

_app = Flask(__name__)

# _app.secret_key = os.environ['FLASK_SECRET_KEY']
_app.secret_key = 'dont-hack-me-pls'


class TextForm(FlaskForm):
	text_input = StringField("Input Text", validators=[DataRequired()])


server_to_text = SafeQueue()


@_app.route("/", methods=("GET", "POST"))
def index():
	form = TextForm()

	if form.validate_on_submit():
		server_to_text.put("{}".format(Message(form.text_input.data)))

	return render_template("base.html", form=form)


class AppThread(Thread):
	def __init__(self):
		super().__init__(daemon=True)
		self.server_to_text = server_to_text

	def run(self) -> None:
		logger.info("Flask App staring")
		_app.run(port=5678)
