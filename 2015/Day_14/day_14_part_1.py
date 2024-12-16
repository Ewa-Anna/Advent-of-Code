puzzle = "input.txt"

with open(puzzle) as f:
    raw_input = [line.strip().split() for line in f]

reindeer = []
for line in raw_input:
    name = line[0]
    speed = int(line[3])
    fly_time = int(line[6])
    rest_time = int(line[-2])
    reindeer.append((name, speed, fly_time, rest_time))


def calculate_distance(speed, fly_time, rest_time, total_seconds):
    cycle_time = fly_time + rest_time
    full_cycles = total_seconds // cycle_time
    remaining_time = total_seconds % cycle_time
    flying_time = full_cycles * fly_time + min(fly_time, remaining_time)
    return flying_time * speed


race_duration = 2503

distances = {}
for name, speed, fly_time, rest_time in reindeer:
    distances[name] = calculate_distance(speed, fly_time, rest_time, race_duration)

winning_reindeer = max(distances, key=distances.get)
winning_distance = distances[winning_reindeer]

print(winning_distance)
