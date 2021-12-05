import random
import numpy as np


class WeatherReport:
    @staticmethod
    def generate_random_weather():
        mu_wind_spd=15

        sigma_wind=7

        mu_temp=50

        sigma_temp=20

        wind_speed=abs(round(np.random.normal(mu_wind_spd, sigma_wind)))

        wind_direction=random.randint(0,359)

        temperature=round(np.random.normal(mu_temp, sigma_temp))

        rain=random.choices([True, False], weights=[.20, .8])[0]

        return WeatherReport(wind_speed, wind_direction, temperature, rain)


    def __init__(self, wind_speed, wind_direction, temperature, rain):
        self.wind_speed = wind_speed

        self.wind_direction = wind_direction

        self.temperature = temperature

        self.rain = rain



class WeatherGenerator:
    def __init__(self):
        self.current_weather = WeatherReport.generate_random_weather()


    def set_weather(self, report):
        self.current_weather = report


