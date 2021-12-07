import unittest
from unittest import mock

import constants
from flightinfo import FlightInfo

class TestFlightInfo(unittest.TestCase):
    def setUp(self) -> None:
        FlightInfo.assigned_flights = set([])

    def tearDown(self) -> None:
        FlightInfo.assigned_flights = set([])

    def test_generate_next_flight(self):
        start_time = 0
        self.assertTrue(len(FlightInfo.assigned_flights) == 0)

        res = FlightInfo(start_time, False)
        self.assertTrue(type(res) == FlightInfo)
        self.assertTrue(res.flight_number in FlightInfo.assigned_flights)
        self.assertTrue(type(res.flight_number) == int and
                        res.flight_number <= constants.FLIGHT_NUMBER_MAX and
                        res.flight_number >= constants.FLIGHT_NUMBER_MIN)
        self.assertTrue(res.departure_time <= start_time + constants.TIME_TO_DEPART_MAX and
                        res.departure_time >= start_time + constants.TIME_TO_DEPART_MIN)
        self.assertTrue(res.arrival_time <= res.departure_time + constants.TIME_TO_ARRIVE_MAX and
                        res.arrival_time >= res.departure_time + constants.TIME_TO_ARRIVE_MIN)

    @mock.patch('flightinfo.randint', create=True)
    def test_generate_next_flight_existing_flight_number(self, mock_rand):
        start_time = 0
        res = FlightInfo(start_time, False)
        self.assertTrue(len(FlightInfo.assigned_flights) == 1)
        mock_rand.side_effect = [res.flight_number]
        
        res.generate_next_flight(start_time, False)
        self.assertTrue(type(res) == FlightInfo)
        self.assertTrue(res.flight_number in FlightInfo.assigned_flights)
        self.assertTrue(type(res.flight_number) == int and
                        res.flight_number <= constants.FLIGHT_NUMBER_MAX and
                        res.flight_number >= constants.FLIGHT_NUMBER_MIN)
        self.assertTrue(res.departure_time <= start_time + constants.TIME_TO_DEPART_MAX and
                        res.departure_time >= start_time + constants.TIME_TO_DEPART_MIN)
        self.assertTrue(res.arrival_time <= res.departure_time + constants.TIME_TO_ARRIVE_MAX and
                        res.arrival_time >= res.departure_time + constants.TIME_TO_ARRIVE_MIN)
        

if __name__ == '__main__':
    unittest.main()