def execute_program(file_path):
    with open(file_path, 'r') as f:
        instructions = [line.strip() for line in f.readlines()]

    registers = {'a': 1, 'b': 0}  
    pointer = 0

    def parse_offset(offset):
        return int(offset)

    while 0 <= pointer < len(instructions):
        parts = instructions[pointer].split()
        instruction = parts[0]

        if instruction == 'hlf':
            # hlf r
            reg = parts[1]
            registers[reg] //= 2
            pointer += 1

        elif instruction == 'tpl':
            # tpl r
            reg = parts[1]
            registers[reg] *= 3
            pointer += 1

        elif instruction == 'inc':
            # inc r
            reg = parts[1]
            registers[reg] += 1
            pointer += 1

        elif instruction == 'jmp':
            # jmp offset
            offset = parse_offset(parts[1])
            pointer += offset

        elif instruction == 'jie':
            # jie r, offset
            reg = parts[1].strip(',')
            offset = parse_offset(parts[2])
            if registers[reg] % 2 == 0:
                pointer += offset
            else:
                pointer += 1

        elif instruction == 'jio':
            # jio r, offset
            reg = parts[1].strip(',')
            offset = parse_offset(parts[2])
            if registers[reg] == 1:
                pointer += offset
            else:
                pointer += 1

    return registers['b']

if __name__ == "__main__":
    result = execute_program("input.txt")
    print("Value in register b:", result)
