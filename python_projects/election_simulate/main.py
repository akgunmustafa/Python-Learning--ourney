# Simulate the results of an election using a Monte Carlo simulation

# We have 2 candidates (left and right) and 3 regions
# Region 1: 87% chance of winning 'Left'
# Region 1: 65% chance of winning 'Left'
# Region 3: 17% chance of winning 'Left'

# This program simulates the election 10,000 times and prints the percentage of where Candidate 'Left' wins.


from random import random

num_times_left_wins = 0
num_times_right_wins = 0
num_trials = 10_000
for trial in range(0, num_trials):
    votes_for_left = 0
    votes_for_right = 0

    # Determine who wins the 1st region
    if random() < 0.87:
        votes_for_left += 1
    else:
        votes_for_right += 1

    # Determine who wins the 2nd region
    if random() < 0.65:
        votes_for_left += 1
    else:
        votes_for_right += 1

    # Determine who wins the 3rd region
    if random() < 0.17:
        votes_for_left += 1
    else:
        votes_for_right += 1

    # Determine overall election outcome
    if votes_for_left > votes_for_right:
        num_times_left_wins += 1
    else:
        num_times_right_wins += 1

print(f"Probability Left wins: {num_times_left_wins / num_trials} ")
print(f"Probability Right wins: {num_times_right_wins / num_trials}")
