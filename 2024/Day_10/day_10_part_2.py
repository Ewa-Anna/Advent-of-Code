from day_10_part_1 import topographic_map


def calculate_trailhead_ratings(topographic_map):
    grid = [[int(char) for char in line] for line in topographic_map.strip().split("\n")]
    rows, cols = len(grid), len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    memo = {}

    def dfs(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        
        current_height = grid[x][y]
        if current_height == 9:
            return 1  

        total_paths = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:  
                if grid[nx][ny] == current_height + 1:  
                    total_paths += dfs(nx, ny)

        memo[(x, y)] = total_paths
        return total_paths

    total_rating = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:  
                total_rating += dfs(r, c)
    
    return total_rating

result = calculate_trailhead_ratings(topographic_map)
print(result)
