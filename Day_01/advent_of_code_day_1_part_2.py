calibration_document = "advent_of_code_day_1_puzzle.txt"

with open(calibration_document) as f:
    puzzle_input = [line.rstrip().lower() for line in f]

mapping = {"one": "o1e",
           "two": "t2o",
           "three": "t3e",
           "four": "f4r",
           "five": "f5e",
           "six": "s6x",
           "seven": "s7n",
           "eight": "e8t",
           "nine": "n9e"
           }

converted_puzzle_input = ",".join(str(element) for element in puzzle_input)

for key, value in mapping.items():
    converted_puzzle_input = converted_puzzle_input.replace(key, str(value))


def calibration(converted_puzzle_input):
    total = 0
    for line in converted_puzzle_input:
        answer = []
        for i in line:
            if i.isdigit():
                answer.append(i)
        answer = answer[0] + answer[-1]
        total += int(answer)
    return total


print(calibration(list(converted_puzzle_input.split(","))))
