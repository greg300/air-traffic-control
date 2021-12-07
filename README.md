# ECE567_Team11_Major
Software Engineering 567, Team 11, Major Project.

---

## How to Run
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
