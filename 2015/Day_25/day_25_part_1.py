def calculate_code(row, col):
    initial_code = 20151125
    multiplier = 252533
    modulus = 33554393

    position = (row + col - 2) * (row + col - 1) // 2 + col

    code = initial_code
    for _ in range(position - 1):
        code = (code * multiplier) % modulus

    return code

if __name__ == "__main__":
    row, col = 2978, 3083
    result = calculate_code(row, col)
    print("The code for the machine is:", result)
