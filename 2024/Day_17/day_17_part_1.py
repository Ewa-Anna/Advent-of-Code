def parse_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    A = B = C = 0
    for line in lines:
        if line.startswith("Register A"):
            A = int(line.split(":")[1].strip())
        elif line.startswith("Register B"):
            B = int(line.split(":")[1].strip())
        elif line.startswith("Register C"):
            C = int(line.split(":")[1].strip())

    program = []
    for line in lines:
        if line.startswith("Program"):
            program_str = line.split(":")[1].strip()
            program = list(map(int, program_str.split(",")))
            break

    return (A, B, C), program

def execute_program(registers, program):
    A, B, C = registers
    output = []
    ip = 0  # Instruction pointer

    def resolve_combo_operand(operand):
        if operand < 4:  
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        elif operand == 7:
            raise ValueError("Invalid combo operand 7 encountered.")

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1] if ip + 1 < len(program) else None

        if opcode == 0: 
            divisor = 2 ** resolve_combo_operand(operand)
            A //= divisor

        elif opcode == 1:
            B ^= operand

        elif opcode == 2:
            B = resolve_combo_operand(operand) % 8

        elif opcode == 3:
            if A != 0:
                ip = operand
                continue 

        elif opcode == 4:
            B ^= C

        elif opcode == 5:  
            output.append(resolve_combo_operand(operand) % 8)

        elif opcode == 6:  
            divisor = 2 ** resolve_combo_operand(operand)
            B = A // divisor

        elif opcode == 7:  
            divisor = 2 ** resolve_combo_operand(operand)
            C = A // divisor

        else:
            raise ValueError(f"Unknown opcode {opcode} encountered.")

        ip += 2

    return ",".join(map(str, output))

if __name__ == "__main__":
    input_file = "input.txt"
    registers, program = parse_input_file(input_file)

    result = execute_program(registers, program)
    print(result)
