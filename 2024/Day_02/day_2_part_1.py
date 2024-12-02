puzzle = "input.txt"

with open(puzzle) as f:
    raw_input = [list(map(int, line.strip().split())) for line in f]

def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    if not all(-3 <= diff <= 3 and diff != 0 for diff in differences):
        return False
    
    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all(diff < 0 for diff in differences)
    
    return all_increasing or all_decreasing


safe_count = sum(is_safe(report) for report in raw_input)

print(safe_count)