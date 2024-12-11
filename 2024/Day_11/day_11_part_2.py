from collections import defaultdict
from day_11_part_1 import initial_stones


def optimized_blink_stones(initial_stones, blinks):
    stone_counts = defaultdict(int)
    for stone in initial_stones:
        stone_counts[stone] += 1

    for _ in range(blinks):
        new_counts = defaultdict(int)
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                mid = len(digits) // 2
                left = int(digits[:mid])
                right = int(digits[mid:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_stone = stone * 2024
                new_counts[new_stone] += count
        stone_counts = new_counts

    return sum(stone_counts.values())

blinks = 75

total_stones = optimized_blink_stones(initial_stones, blinks)
print(total_stones)
