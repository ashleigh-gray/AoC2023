import numpy as np

testing = False

if testing:
    records = [(7, 9), (15, 40), (30, 200)]
elif not testing:
    records = [(41, 214), (96, 1789), (88, 1127), (94, 1055)]

results = []
for time, distance in records:
    ways_to_win = 0
    for option in range(0,time):
        hold_time = option
        travel_time = time - option
        predicted_distance = hold_time*travel_time
        if predicted_distance > distance:
            ways_to_win += 1

    results.append(ways_to_win)
print(results)
print(np.prod(results))
