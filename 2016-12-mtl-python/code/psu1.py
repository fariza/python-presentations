class PSU:
    def __init__(self):
        self._voltage = 0
        self._on = False

    @property
    def voltage(self):
        return self._voltage * self._on

    @voltage.setter
    def voltage(self, value):
        self._voltage = value

    def turn_on(self):
        self._on = True
