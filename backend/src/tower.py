import copy
import random
from queue import Queue

from airport import Airport
from airplane import Airplane
from weathergenerator import WeatherGenerator


class Tower:
    def __init__(self,
                 num_planes: int,
                 num_gates: int,
                 weather_generator: WeatherGenerator,
                 num_departure_spots: int = 6,
                 num_arrival_spots: int = 6,
                 num_landing_spots: int = 6):
        self._time = 1

        self._airport = Airport(num_gates)

        self._planes = {}

        for i in range(1, num_planes + 1):
            # randomly initialize a new airplane as either
            # at the gate or in flightxs
            at_gate = random.randint(0, 1) == 1

            gate = None
            if at_gate and self._airport.num_available_gates():
                # a plane starts "AtGate" if it is initialized
                # with a gate assignment
                gate = self._airport.assign_gate()

            self._planes[i] = Airplane(i,
                                       self._time,
                                       self,
                                       gate)

        self._weather_generator = weather_generator

        self._current_weather = self._weather_generator.current_weather

        self._departure_q = Queue(num_departure_spots)

        self._arrival_q = Queue(num_arrival_spots)

        self._landing_q = Queue(num_landing_spots)


    def _weather_ok(self):
        # TODO, evaluate current weather for ok to proceed
        # conditions for departure or arrival
        return True


    def step_time(self):
        self._time += 1

        current_weather = self._weather_generator.current_weather

        self._departure_q.advance()

        self._arrival_q.advance()

        self._landing_q.advance()

        for _, plane in sorted(self._planes.items()):
            plane.step_time(self._time)


    def state(self):
        return self._planes.values()


    def request_slot_for_departure(self, plane: Airplane) -> bool:
        # clear plane for departure if there is a spot at
        # the end of the departure queue
        if not self._departure_q.can_add():
            return False

        self._departure_q.push_back(plane)

        return True


    def request_clear_for_takeoff(self, plane: Airplane) -> bool:
        # clear flane for takeoff if it is in front of the
        # departure queue and weather is ok
        if not self._weather_ok():
            return False

        if not plane == self._departure_q.front:
            return False

        self._departure_q.pop_front()

        return True


    def request_slot_for_landing(self, plane: Airplane) -> bool:
        # request slot for landing if there is a spot at
        # the end of the landing queue
        if not self._landing_q.can_add():
            return False

        self._landing_q.push_back(plane)

        return True


    def request_clear_for_landing(self, plane: Airplane) -> bool:
        # allow a plane to land if it is at the front of
        # the landing queue and weather is ok
        if self._landing_q.front == plane:
            self._arrival_q.push_back(plane)
            self._landing_q.pop_front()

            return True

        return False


    def request_gate(self, plane: Airplane) -> int:
        if self._arrival_q.front == plane:
            return self._airport.assign_gate()

        return None
