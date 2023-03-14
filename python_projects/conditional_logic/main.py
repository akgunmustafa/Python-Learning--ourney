# Simulate Events and Calculate Probabilities

from random import randint

#This function that simulate the roll of a die.
def roll():
    """Return random integer between 1 and 6"""
    return randint(1, 6)

#Simulate 10.000 rolls and calculate average
num_rolls = 10_000
total = 0

for trial in range(num_rolls):
    total += roll()

average_roll = total/num_rolls

print(f"The average result of {num_rolls} rolls is {average_roll} ")

