from airplane import Airplane


class Queue:
    def __init__(self, num_slots):
        self._q = [ None ] * num_slots
        self._front = None


    def advance(self):
        if self._q[0]:
            self._front = self._q[0]
            self._q[0] = None

        for i in range(len(self._q) - 1):
            if self._q[i] is None:
                self._q[i] = self._q[i + 1]
                self._q[i + 1] = None


    @property
    def front(self):
        return self._front


    def pop_front(self):
        f = self._front
        self._front = None
        return f


    def can_add(self):
        return self._q[len(self._q)-1] is None


    def push_back(self, a: Airplane):
        if not self.can_add():
            raise ValueError('No space!')

        self._q[len(self._q)-1] = a


    def index(self, a: Airplane):
        if not self._q.count(a):
            return None
        else:
            return self._q.index(a)
