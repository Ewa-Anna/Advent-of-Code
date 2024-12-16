from day_14_part_1 import reindeer, race_duration


points = {name: 0 for name, _, _, _ in reindeer}
distances = {name: 0 for name, _, _, _ in reindeer}

for t in range(1, race_duration + 1):
    for name, speed, fly_time, rest_time in reindeer:
        cycle_time = fly_time + rest_time
        if (t % cycle_time) <= fly_time and (t % cycle_time) != 0:
            distances[name] += speed
    max_distance = max(distances.values())

    for name in distances:
        if distances[name] == max_distance:
            points[name] += 1

winning_reindeer = max(points, key=points.get)
winning_points = points[winning_reindeer]

print(winning_points)
