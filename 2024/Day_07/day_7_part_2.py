from itertools import product
from day_7_part_1 import input_data


def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
        elif operator == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def can_match_test_value(test_value, numbers):
    num_operators = len(numbers) - 1
    for operators in product(['+', '*', '||'], repeat=num_operators):
        try:
            if evaluate_expression(numbers, operators) == test_value:
                return True
        except Exception as e:
            continue
    return False

def total_calibration_result(input_data):
    total = 0
    for line in input_data.splitlines():
        if not line.strip():
            continue  
        test_value, numbers = line.split(":")
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))
        
        if can_match_test_value(test_value, numbers):
            total += test_value
    return total

result = total_calibration_result(input_data)
print(result)
