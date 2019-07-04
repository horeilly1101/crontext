"""File that contains our TextModel class."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP
from flask_migrate import Migrate

db = SQLAlchemy()  # create the database
migrate = Migrate(db)


class TextModel(db.Model):
	"""Model class to describe and keep track of text messages."""
	id = db.Column(INTEGER, primary_key=True, index=True)
	message = db.Column(TEXT)  # string text message
	created_at = db.Column(TIMESTAMP, default=datetime.utcnow)
	sent_at = db.Column(TIMESTAMP, default=None)
