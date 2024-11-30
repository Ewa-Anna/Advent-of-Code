import json

puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = f.read()


try:
    parsed_json = json.loads(puzzle_input)
except json.JSONDecodeError as e:
    parsed_json = None
    error_message = str(e)


def sum_numbers(data):
    if isinstance(data, int) or isinstance(data, float):
        return data
    elif isinstance(data, list):
        return sum(sum_numbers(item) for item in data)
    elif isinstance(data, dict):
        return sum(sum_numbers(value) for value in data.values())
    return 0


if parsed_json is not None:
    total_sum = sum_numbers(parsed_json)
else:
    total_sum = None

total_sum, error_message if parsed_json is None else None

print(total_sum)
