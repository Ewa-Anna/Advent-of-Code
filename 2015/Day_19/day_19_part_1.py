def parse_input(file_path):
    with open(file_path, "r") as file:
        input_data = file.read()

    lines = input_data.strip().splitlines()

    starting_molecule = lines[-1]

    replacements = []
    for line in lines[:-1]:
        line = line.strip()
        if not line:
            continue

        if " => " in line:
            old, new = line.split(" => ")
            replacements.append((old, new))

    return replacements, starting_molecule


def count_distinct_molecules(replacements, molecule):
    distinct_molecules = set()

    for old, new in replacements:
        start = 0
        while start < len(molecule):
            start = molecule.find(old, start)
            if start == -1:
                break

            new_molecule = molecule[:start] + new + molecule[start + len(old) :]
            distinct_molecules.add(new_molecule)

            start += 1

    return len(distinct_molecules)


input_file_path = "input.txt"

replacements, starting_molecule = parse_input(input_file_path)

result = count_distinct_molecules(replacements, starting_molecule)

print(result)
