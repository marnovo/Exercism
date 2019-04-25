#
# Exercism.io
# Python track
# Problem #3 - Clock
# github.com/marnovo/Exercism
#

HOURS_IN_DAY = 24
MINS_IN_HOUR = 60


class Clock(object):

    def __init__(self, hours, minutes, add_min=0):
        total_min = hours * MINS_IN_HOUR + minutes + add_min
        self.hours = (total_min // MINS_IN_HOUR) % HOURS_IN_DAY
        self.minutes = (total_min - self.hours * MINS_IN_HOUR) % MINS_IN_HOUR

    def add(self, minutes):
        self.__init__(self.hours, self.minutes, add_min=minutes)
        return self

    def __eq__(self, comparison):
        return self.__repr__() == comparison.__repr__()

    def __repr__(self):
        return f"{self.hours:02}:{self.minutes:02}"
