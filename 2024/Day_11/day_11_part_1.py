puzzle = "input.txt"

with open(puzzle, "r") as file:
    initial_stones = file.read().strip()
    initial_stones = list(map(int, initial_stones.split(" ")))


def blink_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                mid = len(digits) // 2
                left = int(digits[:mid])
                right = int(digits[mid:])
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones

blinks = 25

resulting_stones = blink_stones(initial_stones, blinks)
print(len(resulting_stones))
