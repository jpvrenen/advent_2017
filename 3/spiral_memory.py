""" Find the distance to 1 """
import math
import numpy as np

puzzle_input = 289326
puzzle_input = 23

def odd_wortel_vinden(data):
    """ Find square number to create matrix """
    while True:
        wortel = math.sqrt(data)
        if not wortel%1:
            if not wortel%2:
                data += 1
            else:
                return wortel
        else:
            data += 1

odd_wrtl = int(odd_wortel_vinden(puzzle_input))
print odd_wrtl

a = np.arange(odd_wrtl**2).reshape(odd_wrtl,odd_wrtl)
print a
