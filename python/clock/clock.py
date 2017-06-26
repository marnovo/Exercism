#
# Exercism.io
# Python track
# Problem #3 - Clock
# github.com/marnovo/Exercism
#

class Clock(object):
   
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add(self, minutes):
        self.minutes = self.minutes + minutes
        return #check what to return, if string or not
