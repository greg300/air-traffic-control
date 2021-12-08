# coding=utf-8

from flask import Flask

import constants
from tower import Tower
from weathergenerator import WeatherGenerator


# Create the Flask application.
app = Flask(__name__)

wg = WeatherGenerator()

# Only show good weather case to start
wg.current_weather.rain = False

tower = Tower(constants.NUM_PLANES,
              constants.NUM_GATES,
              wg)



def to_html(now, departures, arrivals):
    html = '<head>'
    html += '<title>ATCS</title>'
    html += '<link rel="stylesheet" href="/static/css/style.css">'
    html += '</head>'

    html += '<h4>Departures</h4>'
    html += f'<table>'
    html += f'<tr><th>Plane</th><th>Flight</th><th>Gate</th><th>Time</th><th>Status</th><th>State</th></tr>'
    for plane in departures:
        gate = plane.gate
        if not gate:
            gate = ''
        status = 'On Time' if plane.flight_info.departure_time >= now else 'Delayed'
        html += f'<tr><td>{plane.plane_id}</td><td>{plane.flight_info.flight_number}</td><td>{gate}</td><td>{plane.flight_info.departure_time}</td><td>{status}</td><td>{plane.state}</td></tr>'
    html += f'</table>'

    html += '<h4>Arrivals</h4>'
    html += f'<table>'
    html += f'<tr><th>Plane</th><th>Flight</th><th>Gate</th><th>Time</th><th>Status</th><th>State</th></tr>'
    for plane in arrivals:
        gate = plane.gate
        if not gate:
            gate = ''
        status = 'Delayed'
        if plane.is_arrived:
            status = 'Arrived'
        elif plane.flight_info.arrival_time >= now:
            status = 'On Time'
        html += f'<tr><td>{plane.plane_id}</td><td>{plane.flight_info.flight_number}</td><td>{gate}</td><td>{plane.flight_info.arrival_time}</td><td>{status}</td><td>{plane.state}</td></tr>'
    html += f'</table>'

    return html


@app.route('/next')
def get_next():
    tower.step_time()

    now = tower.time

    return f'<header><h3>Scarlet Knight Airways</h3></header>' + \
        f'<section id="status">' + \
        f'<h4>Time: {now}</h4>' + \
        f'<h4>Weather Hold: {not tower.weather_ok}</h4>' + \
        f'</section>' + \
        f'<section id="flights">' + \
        to_html(now, tower.departures, tower.arrivals) + \
        f'</section>'


@app.route('/')
def get_current():
    now = tower.time

    return f'<header><h3>Scarlet Knight Airways</h3></header>' + \
        f'<section id="status">' + \
        f'<h4>Time: {now}</h4>' + \
        f'<h4>Weather Hold: {not tower.weather_ok}</h4>' + \
        f'</section>' + \
        f'<section id="flights">' + \
        to_html(now, tower.departures, tower.arrivals) + \
        f'</section>'


if __name__=='__main__':
    app.run(debug=True)
