"""defines the structure of the main app"""

import logging
from threading import Thread

from flask_wtf import FlaskForm
from wtforms import StringField
from flask import Flask, render_template
from wtforms.validators import DataRequired

from crontext import lifo

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

_app = Flask(__name__)

_app.secret_key = "asdfghjk"


class TextForm(FlaskForm):
	text_input = StringField("Input Text", validators=[DataRequired()])


@_app.route("/", methods=("GET", "POST"))
def index():
	form = TextForm()

	if form.validate_on_submit():
		lifo.put("user input: {}".format(form.text_input.data))

	return render_template("base.html", form=form)


def target():
	logger.info("Flask App staring")
	_app.run(port=5678)


# put the app in its own thread
app_thread = Thread(target=target, daemon=True)

if __name__ == "__main__":
	# run the app
	_app.run()
