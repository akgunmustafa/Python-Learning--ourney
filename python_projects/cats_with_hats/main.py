cats_with_hats = []

# We want the laps to be from 1 to 100 instead of 0 to 99
for lap in range(1, 101):
    for cat in range(1, 101):

        # Only look at cats that are divisible by the lap
        if cat % lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)

print(cats_with_hats)
