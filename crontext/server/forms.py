from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class TextForm(FlaskForm):
	text_input = StringField("Input Text", validators=[DataRequired()])
