"""File that initializes the database with necessary tables."""

if __name__ == "__main__":
	from crontext.server.models import db
	from crontext.server import create_app

	app = create_app(None, None)

	with app.app_context():
		db.create_all()
