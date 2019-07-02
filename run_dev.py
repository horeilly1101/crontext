"""Run the server for development."""

if __name__ == "__main__":
	# load environment variables
	from dotenv import load_dotenv
	load_dotenv()

	from crontext import run_crontext
	run_crontext("127.0.0.1", 6789)
