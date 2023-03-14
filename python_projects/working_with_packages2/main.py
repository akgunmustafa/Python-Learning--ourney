from helpers.math import area
from helpers.string import shout

length = 5
width = 8

message = f"The are of a {length}-by-{width} rectangle is {area(length, width)}"
print(shout(message))
