import copy

from airport import Airport
from airplane import Airplane
from weathergenerator import WeatherGenerator


class Tower:
    def __init__(self,
                 num_planes: int,
                 num_gates: int,
                 weather_generator: WeatherGenerator):
        self._time = 1

        self._airport = Airport(num_gates)

        self._planes = { i: Airplane(i) for i in range(1, num_planes+1) }

        self._weather_generator = weather_generator

        self._departure_q = []
        self._arrival_q = []


    def step_time(self):
        self._time += 1


    def state(self):
        return copy.deepcopy(self._planes)


    def request_slot_for_departure(self, plane: Airplane) -> bool:
        pass


    def request_clear_for_takeoff(self, plane: Airplane) -> bool:
        pass


    def request_slot_for_arrival(self, plane: Airplane) -> bool:
        pass


    def request_clear_for_landing(self, plane: Airplane) -> bool:
        pass


    def request_gate(self, plane: Airplane) -> int:
        pass




def main():
    """
    conditions=safe

    if(rain==true and temp<34): #if cold and rainy it is not safe for takeoff
        conditions = unsafe

    if(wind_spd>28): #if wind speed greater than 28 kts it is not safe for takeoff
        conditions=unsafe

    print("Conditions are ",conditions,"for takeoff")
    """
    t = Tower(20, 20, WeatherGenerator())

    s = t.state()



if __name__=='__main__':
    main()
