import unittest

from weathergenerator import WeatherReport

class TestWeather(unittest.TestCase):
    def test_generate_random_weather(self):
        res = WeatherReport.generate_random_weather()
        self.assertTrue(type(res) == WeatherReport)
        self.assertTrue(type(res.rain) == bool)
        self.assertTrue(res.wind_speed >= 0)
        self.assertTrue(res.wind_direction >= 0 and res.wind_direction <= 359)


if __name__ == '__main__':
    unittest.main()