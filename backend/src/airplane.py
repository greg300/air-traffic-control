from enum import Enum


class State(Enum):
    AtGate = 1
    TaxiingToRunway = 2
    TakeOff = 3
    InFlight = 4
    Approaching = 5
    Landed = 6
    TaxiingToGate = 7


class Airplane:
    def __init__(self, plane_id):
        self._id = plane_id

        self._state = State.AtGate
