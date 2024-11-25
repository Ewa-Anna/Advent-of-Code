from day_7_part_1 import parse_instruction, get_signal

puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]
    
def solve_circuit_with_override(instructions, target_wire):
    circuit = {}
    for instruction in instructions:
        operation, output = parse_instruction(instruction)
        circuit[output] = operation
    
    cache = {}
    signal_a = get_signal(target_wire, circuit, cache)
    
    circuit['b'] = str(signal_a)
    cache = {}
    
    return get_signal(target_wire, circuit, cache)

updated_result = solve_circuit_with_override(puzzle_input, 'a')
print(f"New signal to wire 'a': {updated_result}")
