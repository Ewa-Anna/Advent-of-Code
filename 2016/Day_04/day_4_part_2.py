from collections import Counter


def parse_room(line):
    last_dash = line.rfind("-")
    sector_id, checksum = line[last_dash + 1 :].strip().split("[")
    name = line[:last_dash].replace("-", " ")
    checksum = checksum.strip("]")
    return name, int(sector_id), checksum


def is_real_room(name, checksum):
    letter_counts = Counter(name.replace(" ", ""))
    sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
    expected_checksum = "".join(letter for letter, _ in sorted_letters[:5])
    return expected_checksum == checksum


def decrypt_name(name, sector_id):
    decrypted = []
    for char in name:
        if char == " ":
            decrypted.append(" ")
        else:
            new_char = chr(((ord(char) - ord("a") + sector_id) % 26) + ord("a"))
            decrypted.append(new_char)
    return "".join(decrypted)


def find_north_pole_room(filename):
    with open(filename, "r") as file:
        for line in file:
            name, sector_id, checksum = parse_room(line)
            if is_real_room(name, checksum):
                decrypted_name = decrypt_name(name, sector_id)
                if "north" in decrypted_name.lower():
                    return sector_id
    return None


filename = "input.txt"
north_pole_sector_id = find_north_pole_room(filename)
print(f"Sector ID of the room with North Pole objects: {north_pole_sector_id}")
