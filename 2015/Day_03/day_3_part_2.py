puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]

puzzle_input = list(puzzle_input[0])

santa_position = (0, 0)
robo_santa_position = (0, 0)

visited_houses = set()

visited_houses.add(santa_position)

for i, direction in enumerate(puzzle_input):
    if i % 2 == 0:  
        if direction == '^':
            santa_position = (santa_position[0], santa_position[1] + 1)  
        elif direction == 'v':
            santa_position = (santa_position[0], santa_position[1] - 1)  
        elif direction == '>':
            santa_position = (santa_position[0] + 1, santa_position[1])  
        elif direction == '<':
            santa_position = (santa_position[0] - 1, santa_position[1])  
        visited_houses.add(santa_position)
    else:  
        if direction == '^':
            robo_santa_position = (robo_santa_position[0], robo_santa_position[1] + 1)  
        elif direction == 'v':
            robo_santa_position = (robo_santa_position[0], robo_santa_position[1] - 1)  
        elif direction == '>':
            robo_santa_position = (robo_santa_position[0] + 1, robo_santa_position[1])  
        elif direction == '<':
            robo_santa_position = (robo_santa_position[0] - 1, robo_santa_position[1])  
        visited_houses.add(robo_santa_position)

print(len(visited_houses))