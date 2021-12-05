import cmd
import constants
from tower import Tower
from weathergenerator import WeatherGenerator


class ATCSShell(cmd.Cmd):
    prompt: str = '<atcs> '

    def __init__(self, num_planes, num_gates):
        super().__init__()

        self._wg = WeatherGenerator()

        self._tower = Tower(num_planes, num_gates, self._wg)

        self._show_status(self._tower.time)


    def do_setrain(self, arg):
        """
        setrain true|false
        """
        if arg.lower() == 'true':
            self._wg.current_weather.rain = True
        elif arg.lower() == 'false':
            self._wg.current_weather.rain = False
        else:
            print(f'Bad argument {arg}, Ignoring')


    def do_step(self, arg):
        """
        Step the system and print the new state.
        """
        self._tower.step_time()

        self._show_status(self._tower.time)


    def _show_status(self, now):
        now = self._tower.time

        print('-------------------')
        print(f'ATCS')
        print(f'Time: {now}')
        print(f'Weather Hold: {not self._tower.weather_ok}')
        print('-------------------')
        print('Departures:')
        print('| Plane  | Flight Num  | Gate  | Departure Time   | Status    | State                     |')
        for plane in self._tower.departures:
            gate = plane.gate if plane.gate else ''
            status = 'On Time' if plane.flight_info.departure_time >= now else 'Delayed'
            print('| {0:>6d} | {1:>11d} | {2:>5s} | {3:>14d}   | {4:<9s} | {5:<25s} |'.format(plane.plane_id,
                                                                                               plane.flight_info.flight_number,
                                                                                               str(gate),
                                                                                               plane.flight_info.departure_time,
                                                                                               status,
                                                                                               plane.state))
        print()
        print('Arrivals:')
        print('| Plane  | Flight Num  | Gate  | Arrival Time     | Status    | State                     |')
        for plane in self._tower.arrivals:
            gate = plane.gate if plane.gate else ''
            status = 'Delayed'
            if plane.is_arrived:
                status = 'Arrived'
            elif plane.flight_info.arrival_time >= now:
                status = 'On Time'
            print('| {0:>6d} | {1:>11d} | {2:>5s} | {3:>14d}   | {4:<9s} | {5:<25s} |'.format(plane.plane_id,
                                                                                              plane.flight_info.flight_number,
                                                                                              str(gate),
                                                                                              plane.flight_info.arrival_time,
                                                                                              status,
                                                                                              plane.state))
        print()


    def do_exit(self, arg):
        """
        Exit and close.
        """
        return True


if __name__=='__main__':
    ATCSShell(constants.NUM_PLANES,
              constants.NUM_GATES).cmdloop()

