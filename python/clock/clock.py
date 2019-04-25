#
# Exercism.io
# Python track
# Problem #3 - Clock
# github.com/marnovo/Exercism
#

import math


class Clock(object):

    HOURS_IN_DAY = 24
    MINS_IN_HOUR = 60

    def __init__(self, hours=0, minutes=0):
        self.hours = hours % Clock.HOURS_IN_DAY
        self.minutes = minutes % Clock.MINS_IN_HOUR
        self.hours = self.hours + math.trunc(minutes / Clock.MINS_IN_HOUR)

    def __repr__(self):
        return f"{self.hours:02}:{self.minutes:02}"
