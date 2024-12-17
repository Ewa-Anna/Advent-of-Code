def get_presents(house_number):
    total_presents = 0
    for elf in range(1, int(house_number**0.5) + 1):
        if house_number % elf == 0:
            total_presents += elf * 10
            if elf != house_number // elf:
                total_presents += (house_number // elf) * 10
    return total_presents

def find_minimum_house(puzzle_input):
    house_number = 1
    while True:
        if get_presents(house_number) >= puzzle_input:
            return house_number
        house_number += 1

with open("input.txt", "r") as file:
    puzzle_input = int(file.read().strip())

result = find_minimum_house(puzzle_input)
print(result)
