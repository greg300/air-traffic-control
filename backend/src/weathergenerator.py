import random
import numpy as np


class WeatherReport:
    def __init__(self):
        mu_wind_spd=15

        sigma_wind=7

        mu_temp=50

        sigma_temp=20

        self.wind_spd=abs(round(np.random.normal(mu_wind_spd, sigma_wind)))

        self.wind_dir=random.randint(0,359)

        self.temp=round(np.random.normal(mu_temp, sigma_temp))

        self.rain=random.choices([True, False], weights=[.20, .8])[0]


class WeatherGenerator:
    def __init__(self):
        self._current_weather = WeatherReport()


