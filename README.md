# crontext
> IN DEVELOPMENT: a task scheduler, for daily motivational texts

Crontext is a small-scale daily text message service. Choose a friend and send them a good morning text every day.

## Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

You can deploy the app to Heroku if you want. Note that the project contains a daemon that will periodically ping
the web server to stop it from sleeping. This will significantly impact your number of free dyno hours given
by Heroku.

## Run Locally

You'll need Python 3 and a Twilio account.

- Start a local PostgreSQL database.

- Clone the repo `git clone http://www.github.com/horeilly1101/crontext` and navigate into the 
directory `cd crontext`.

- Copy and paste the `.env.config` file into a `.env` file in the same directory and set the environment variables
as necessary. (Most importantly, make sure to set the correct database URL.)

- Create a virtual environment `python3 -m venv venv` and source it `. venv/bin/activate`.

- Install the dependencies `pip install -r requirements.txt`.

- Run the server `python3 run_dev.py`.

- Open up `http://localhost:6091` in the browser and enjoy!

## Design

Below is the current (planned) design of the system.

![dashboard](images/crontext-design.png)