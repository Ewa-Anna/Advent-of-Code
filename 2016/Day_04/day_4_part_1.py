from collections import Counter


def parse_room(line):
    last_dash = line.rfind("-")
    sector_id, checksum = line[last_dash + 1 :].strip().split("[")
    name = line[:last_dash].replace("-", "")
    checksum = checksum.strip("]")
    return name, int(sector_id), checksum


def is_real_room(name, checksum):
    letter_counts = Counter(name)
    sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
    expected_checksum = "".join(letter for letter, _ in sorted_letters[:5])
    return expected_checksum == checksum


def sum_real_room_sector_ids(filename):
    total_sector_id = 0

    with open(filename, "r") as file:
        for line in file:
            name, sector_id, checksum = parse_room(line)
            if is_real_room(name, checksum):
                total_sector_id += sector_id

    return total_sector_id


filename = "input.txt"
result = sum_real_room_sector_ids(filename)
print(f"Sum of sector IDs of real rooms: {result}")
