import time as python_time
import numpy as np

t = python_time.time()
testing = False

if testing:
    records = [(71530, 940200)]
elif not testing:
    records = [(41968894, 214178911271055)]

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

elapsed = python_time.time() - t
print("Time taken:", elapsed)