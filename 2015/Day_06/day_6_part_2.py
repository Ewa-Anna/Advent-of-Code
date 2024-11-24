puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]

grid = [[0] * 1000 for _ in range(1000)]
    
for instruction in puzzle_input:
    parts = instruction.split()
    if parts[0] == "toggle":
        action = "toggle"
        x1, y1 = map(int, parts[1].split(','))
        x2, y2 = map(int, parts[3].split(','))
    else:
        action = "turn on" if parts[1] == "on" else "turn off"
        x1, y1 = map(int, parts[2].split(','))
        x2, y2 = map(int, parts[4].split(','))
    
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == "turn on":
                grid[x][y] += 1
            elif action == "turn off":
                grid[x][y] = max(0, grid[x][y] - 1)
            elif action == "toggle":
                grid[x][y] += 2

brightness = sum(sum(row) for row in grid)

print("Brightness:", brightness)
