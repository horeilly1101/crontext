"""Run the server for development. Configure the port in the .env file."""

if __name__ == "__main__":
	# load environment variables
	from dotenv import load_dotenv
	load_dotenv()

	import os
	from crontext import run_crontext
	run_crontext("127.0.0.1", os.environ["PORT"])
