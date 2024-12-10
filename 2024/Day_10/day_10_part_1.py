from collections import deque

puzzle = "input.txt"

with open(puzzle, "r") as file:
    topographic_map = file.read()


def calculate_trailhead_scores(topographic_map):
    grid = [[int(char) for char in line] for line in topographic_map.strip().split("\n")]
    rows, cols = len(grid), len(grid[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(trailhead):
        queue = deque([trailhead])
        visited = set([trailhead])
        reachable_nines = set()
        
        while queue:
            x, y = queue.popleft()
            current_height = grid[x][y]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols: 
                    if (nx, ny) not in visited and grid[nx][ny] == current_height + 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        if grid[nx][ny] == 9:
                            reachable_nines.add((nx, ny))

        return len(reachable_nines)

    total_score = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:  
                total_score += bfs((r, c))
    
    return total_score


result = calculate_trailhead_scores(topographic_map)
print(result)
