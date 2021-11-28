import random
import constants

class FlightInfo:
    # Keep track of all currently assigned flight numbers
    # to prevent duplicates
    assigned_flights = set([])


    def __init__(self, time: int, inflight: bool):
        self._flight_number: int = None

        self._arrival_time: int = 0

        self._departure_time: int = 0

        self.generate_next_flight(time, inflight)


    def generate_next_flight(self, time, inflight):
        if self._flight_number:
            FlightInfo.assigned_flights.discard(self._flight_number)

        next_flight = random.randint(constants.FLIGHT_NUMBER_MIN,
                                     constants.FLIGHT_NUMBER_MAX)

        while next_flight in FlightInfo.assigned_flights:
            next_flight = random.randint(constants.FLIGHT_NUMBER_MIN,
                                         constants.FLIGHT_NUMBER_MAX)

        FlightInfo.assigned_flights.add(next_flight)

        self._flight_number = next_flight

        self._departure_time = time + random.randint(6, 20)

        self._arrival_time = self._departure_time + random.randint(12, 60)


    @property
    def flight_number(self):
        return self._flight_number


    @property
    def departure_time(self):
        return self._departure_time


    @property
    def arrival_time(self):
        return self._arrival_time

