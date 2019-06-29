from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TextForm(FlaskForm):
	text_input = StringField("Input Text", validators=[DataRequired()])
	button = StringField()
