from day_19_part_1 import parse_input

replacements, medicine = parse_input("input.txt")


def molecule_generation(replacements, target_molecule):
    medicine = target_molecule
    count = 0

    while medicine != "e":
        for source, replacement in replacements:
            if replacement in medicine:
                medicine = medicine.replace(replacement, source, 1)
                count += 1
                break
    return count


steps = molecule_generation(replacements, medicine)

print(steps)
