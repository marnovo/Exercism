#
# Exercism.io
# Python track
# Problem #3 - Clock
# github.com/marnovo/Exercism
#

HOURS_IN_DAY = 24
MINS_IN_HOUR = 60


class Clock(object):

    def __init__(self, hours, minutes):
        total_min = hours * MINS_IN_HOUR + minutes
        self.hours = (total_min // MINS_IN_HOUR) % HOURS_IN_DAY
        self.minutes = (total_min - self.hours * MINS_IN_HOUR) % MINS_IN_HOUR

    def __add__(self, minutes):
        return self.__class__(self.hours, self.minutes + minutes)

    def __sub__(self, minutes):
        return self.__class__(self.hours, self.minutes - minutes)

    def __eq__(self, comparison):
        return self.__repr__() == comparison.__repr__()

    def __repr__(self):
        return f"{self.hours:02}:{self.minutes:02}"
