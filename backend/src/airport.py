
class Airport:
    def __init__(self, num_gates):
        self._num_gates = num_gates

        self._available_gates = set(range(1, num_gates + 1))

        self._assigned_gates = set([])


    def num_available_gates(self):
        return len(self._available_gates)


    def assign_gate(self):
        if self._available_gates:
            gate = list(self._available_gates)[0]

            self._available_gates.remove(gate)

            self._assigned_gates.add(gate)

            return gate

        return None


    def replace_gate(self, gate):
        self._assigned_gates.remove(gate)

        self._available_gates.add(gate)
