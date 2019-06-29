"""File that contains our TextModel class."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP

db = SQLAlchemy()  # create the database


class TextModel(db.Model):
	"""Model class to describe and keep track of text messages."""
	id = db.Column(INTEGER, primary_key=True, index=True)
	message = db.Column(TEXT)
	created_at = db.Column(TIMESTAMP, default=datetime.utcnow)
	sent_at = db.Column(TIMESTAMP, default=None)
