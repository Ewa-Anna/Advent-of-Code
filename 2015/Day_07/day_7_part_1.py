puzzle = "input.txt"

with open(puzzle) as f:
    puzzle_input = [line.rstrip() for line in f]

def parse_instruction(instruction):
    parts = instruction.split(" -> ")
    operation = parts[0]
    output = parts[1]
    return operation, output

def get_signal(wire, circuit, cache):
    if wire in cache:
        return cache[wire]
    
    if wire.isdigit():
        return int(wire)
    
    operation = circuit[wire]
    if "AND" in operation:
        left, right = operation.split(" AND ")
        result = get_signal(left, circuit, cache) & get_signal(right, circuit, cache)
    elif "OR" in operation:
        left, right = operation.split(" OR ")
        result = get_signal(left, circuit, cache) | get_signal(right, circuit, cache)
    elif "LSHIFT" in operation:
        left, shift = operation.split(" LSHIFT ")
        result = get_signal(left, circuit, cache) << int(shift)
    elif "RSHIFT" in operation:
        left, shift = operation.split(" RSHIFT ")
        result = get_signal(left, circuit, cache) >> int(shift)
    elif "NOT" in operation:
        _, operand = operation.split("NOT ")
        result = ~get_signal(operand, circuit, cache) & 0xFFFF  
    else:
        result = get_signal(operation, circuit, cache)
    
    cache[wire] = result
    return result

def solve_circuit(instructions, target_wire):
    circuit = {}
    for instruction in instructions:
        operation, output = parse_instruction(instruction)
        circuit[output] = operation
    
    cache = {}
    
    return get_signal(target_wire, circuit, cache)

result = solve_circuit(puzzle_input, 'a')
print(f"Signal to wire 'a': {result}")
