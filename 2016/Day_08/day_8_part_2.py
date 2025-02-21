from day_8_part_1 import parse_instruction


def apply_instruction(screen, instruction):
    if instruction[0] == "rect":
        a, b = instruction[1], instruction[2]
        for y in range(b):
            for x in range(a):
                screen[y][x] = 1

    elif instruction[0] == "rotate_row":
        y, by = instruction[1], instruction[2]
        screen[y] = screen[y][-by:] + screen[y][:-by]

    elif instruction[0] == "rotate_column":
        x, by = instruction[1], instruction[2]
        col = [screen[y][x] for y in range(6)]
        col = col[-by:] + col[:-by]
        for y in range(6):
            screen[y][x] = col[y]


def decode_screen(screen):
    letter_map = {
        "011001001010010111101001010010": "A",
        "111001001011100100101001011100": "B",
        "011001001010000100001001001100": "C",
        "111001001010010100101001011100": "D",
        "111101000011100100001000011110": "E",
        "111101000011100100001000010000": "F",
        "011001001010000101101001001110": "G",
        "100101001011110100101001010010": "H",
        "111000100001000010000100011100": "I",
        "001100001000010000101001001100": "J",
        "100101010011000101001010010010": "K",
        "100001000010000100001000011110": "L",
        "100111011010101100101001010010": "M",
        "100111001010110100101001010010": "N",
        "011001001010010100101001001100": "O",
        "111001001010010111001000010000": "P",
        "011001001010010100101011001110": "Q",
        "111001001010010111001010010010": "R",
        "011001001000100001001001001100": "S",
        "111110010000100001000010000100": "T",
        "100101001010010100101001001100": "U",
        "100101001010010100100110000100": "V",
        "100101001010101101011010010010": "W",
        "100101001001100011001001010010": "X",
        "100101001001100001000010000100": "Y",
        "111100001000100010001000011110": "Z",
    }


width, height = 50, 6
screen = [[0] * width for _ in range(height)]

with open("input.txt") as file:
    for line in file:
        instruction = parse_instruction(line.strip())
        apply_instruction(screen, instruction)

print(f"The screen displays:")
for row in screen:
    print("".join("#" if pixel else "." for pixel in row))
