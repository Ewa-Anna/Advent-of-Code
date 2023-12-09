calibration_document = "advent_of_code_day_1_puzzle.txt"

with open(calibration_document) as f:
    puzzle_input = [line.rstrip() for line in f]


def calibration(puzzle_input):
    total = 0
    for line in puzzle_input:
        answer = []
        for i in line:
            if i.isdigit():
                answer.append(i)
        answer = answer[0] + answer[-1]
        total += int(answer)
    return total


print(calibration(puzzle_input))
