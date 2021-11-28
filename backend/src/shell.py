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


    def do_step(self, arg):
        """
        Step the system and print the new state.
        """
        self._tower.step_time()

        state = self._tower.state()

        print('| Plane  | Flight Num  | Gate  | State                     |')
        for airplane in state:
            print(airplane)


    def do_exit(self, arg):
        """
        Exit and close.
        """
        return True


if __name__=='__main__':
    ATCSShell(constants.NUM_PLANES,
              constants.NUM_GATES).cmdloop()

