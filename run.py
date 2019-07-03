"""Run the server for production. (This file is meant to be run when the app is deployed.
You probably don't want to run it locally. Check out run_dev.py instead.)
"""

if __name__ == "__main__":
    import os
    from crontext import run_crontext

    run_crontext("0.0.0.0", os.environ["PORT"])
