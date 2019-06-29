"""File that initializes the database with necessary tables."""

if __name__ == "__main__":
	from crontext.server.models import db
	db.create_all()
