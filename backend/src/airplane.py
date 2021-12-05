from enum import Enum
import random

import constants
from flightinfo import FlightInfo


class State(Enum):
    AtGateArrived = 0
    AtGateDeparting = 1
    TaxiingToRunway = 2
    TakeOff = 3
    InFlight = 4
    Approaching = 5
    Landed = 6
    TaxiingToGate = 7


class Airplane:
    def __init__(self, plane_id, time, tower, gate=None):
        self._handlers = {
            State.AtGateArrived: self.state_at_gate_arrived,
            State.AtGateDeparting: self.state_at_gate_departing,
            State.TaxiingToRunway: self.state_taxiing_to_runway,
            State.TakeOff: self.state_take_off,
            State.InFlight: self.state_in_flight,
            State.Approaching: self.state_approaching,
            State.Landed: self.state_landed,
            State.TaxiingToGate: self.state_taxiing_to_gate
        }

        self._id = plane_id

        # general purpose counter, right now for
        # idle state only
        self._counter = 0

        self._tower = tower

        self._gate = gate

        self._flight_info = FlightInfo(time, gate is None)

        if gate:
            self._state = State.AtGateDeparting
        else:
            self._state = State.InFlight

    @property
    def is_departing(self):
        return self._state in [ State.AtGateDeparting,
                                State.TaxiingToRunway,
                                State.TakeOff ]

    @property
    def is_arriving(self):
        return self._state in [ State.InFlight,
                                State.Approaching,
                                State.Landed,
                                State.TaxiingToGate,
                                State.AtGateArrived ]

    @property
    def is_arrived(self):
        return self._state in [ State.AtGateArrived ]


    @property
    def plane_id(self):
        return self._id


    @property
    def flight_info(self):
        return self._flight_info


    @property
    def gate(self):
        return self._gate


    @property
    def state(self):
        return self._state


    def step_time(self, time):
        self._handlers[self._state](time)


    def state_at_gate_arrived(self, time):
        self._counter -= 1

        if self._counter <= 0:
            self._flight_info.generate_next_flight(time, False)

            self._state = State.AtGateDeparting


    def state_at_gate_departing(self, time):
        time_to_departure = self._flight_info.departure_time - time

        if time_to_departure <= self._tower.departure_lead_time:
            if self._tower.request_slot_for_departure(self):
                self._state = State.TaxiingToRunway
                # release the gate
                self._tower.replace_gate(self._gate)

                self._gate = None


    def state_taxiing_to_runway(self, time):
        if self._tower.request_clear_for_takeoff(self):
            self._state = State.TakeOff


    def state_take_off(self, time):
        self._state = State.InFlight


    def state_in_flight(self, time):
        time_to_arrival = self._flight_info.arrival_time - time

        if time_to_arrival <=  self._tower.arrival_lead_time:
            if self._tower.request_slot_for_landing(self):
                self._state = State.Approaching


    def state_approaching(self, time):
        if self._tower.request_clear_for_landing(self):
            self._state = State.Landed


    def state_landed(self, time):
        self._state = State.TaxiingToGate


    def state_taxiing_to_gate(self, time):
        gate = self._tower.request_gate(self)

        if gate:
            self._gate = gate

            self._counter = random.randint(constants.IDLE_TIME_MIN,
                                           constants.IDLE_TIME_MAX)

            self._state = State.AtGateArrived


    def __str__(self):
        return '| {0:>6d} | {1:>11d} | {2:>5s} | {3:<25s} |'.format(self._id,
                                                                    self._flight_info.flight_number,
                                                                    str(self._gate),
                                                                    self._state)
