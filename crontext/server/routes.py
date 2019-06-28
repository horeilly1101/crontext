from flask import render_template

from crontext.message import Message
from crontext.server import _app, TextForm, server_to_text


@_app.route("/", methods=("GET", "POST"))
def index():
	form = TextForm()

	if form.validate_on_submit():
		server_to_text.put("{}".format(Message(form.text_input.data)))

	return render_template("base.html", form=form)