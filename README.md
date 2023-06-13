# Air Traffic Control System
## ECE 567 - Software Engineering

An air traffic control system prototyping management of takeoffs, taxi between gates and runway, and communication between the tower and up to 20 aircraft at one time. Developed by a team of four via an Agile development model conducted over 3 sprints.

## Team Members
Gregory Giovannini – <gregory.giovannini@rutgers.edu>

Ian Herrighty – <imh30@scarletmail.rutgers.edu>

Dawn Park – <dp863@scarletmail.rutgers.edu>

Eric Schreiber – <ews44@scarletmail.rutgers.edu>

## Usage
### macOS Monterey
#### 1. Install pipenv (virtual Python environment package) for Python 3:
`$ pip install pipenv`  # May need to use `pip3 install pipenv` depending on PATH configuration!

#### 2. Run virtual environment shell:
In `backend` directory, run: 

`$ pipenv shell`

#### 3. Launch ATCS shell OR localhost frontend:
To launch Terminal-based shell:

`$ python src/shell.py`

To launch frontend on localhost:

`$ python src/main.py`

Navigate to `localhost:5000/atcs` (`http://127.0.0.1:5000/atcs`).

Refresh page to "step" time.

#### Testing
To run unit tests:

`$ python src/x`

where x is one of:
* test_flightinfo.py
* test_weather.py
