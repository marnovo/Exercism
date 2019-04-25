#
# Exercism.io
# Python track
# Problem #2 (old track) - Leap year
# github.com/marnovo/Exercism
#

year = int(input("Give a year number: "))


def is_leap_year(year):
    if year % 4 == 0:            # on every year that is evenly divisible by 4
        if year % 100 == 0:      # except every year that is evenly divisible by 100
            if year % 400 == 0:  # unless the year is also evenly divisible by 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap_year(year))
