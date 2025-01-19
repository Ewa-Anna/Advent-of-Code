from day_3_part_1 import is_valid_triangle

def count_valid_triangles_by_columns(filename):
    valid_count = 0
    triangles = []
    
    with open(filename, 'r') as file:
        rows = [list(map(int, line.split())) for line in file]
        
    for col in range(3):
        for i in range(0, len(rows), 3):
            if i + 2 < len(rows):
                triangle = [rows[i][col], rows[i + 1][col], rows[i + 2][col]]
                if is_valid_triangle(triangle):
                    valid_count += 1

    return valid_count

filename = 'input.txt'
valid_triangles = count_valid_triangles_by_columns(filename)
print(f"Number of valid triangles (by columns): {valid_triangles}")
