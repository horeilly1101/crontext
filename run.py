"""Run the server."""

if __name__ == "__main__":
    import os
    from crontext import run_crontext

    run_crontext("0.0.0.0", os.environ["PORT"])
