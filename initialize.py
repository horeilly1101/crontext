"""File that initializes the database with necessary tables."""

if __name__ == "__main__":
	from dotenv import load_dotenv
	load_dotenv()

	from crontext.server.models import db
	from crontext.server import create_app
	from crontext.safe_queue import SafeQueue

	# create a dummy app
	app = create_app(SafeQueue(), SafeQueue())

	# create necessary database tables
	with app.app_context():
		db.create_all()
