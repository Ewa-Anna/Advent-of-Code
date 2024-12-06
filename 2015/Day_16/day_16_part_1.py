mfcsam_results = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse_aunt_sues(file_path):
    aunt_sues = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(": ", 1)
            sue_id = int(parts[0].split()[1])
            attributes = parts[1].split(", ")
            attribute_dict = {}
            for attribute in attributes:
                key, value = attribute.split(": ")
                attribute_dict[key] = int(value)
            aunt_sues[sue_id] = attribute_dict
    return aunt_sues


def find_matching_sue(aunt_sues, mfcsam_results):
    for sue_id, attributes in aunt_sues.items():
        if all(mfcsam_results.get(attr, value) == value for attr, value in attributes.items()):
            return sue_id
    return None


matching_sue = find_matching_sue(parse_aunt_sues("input.txt"), mfcsam_results)
print(matching_sue)
