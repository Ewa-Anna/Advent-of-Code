import hashlib


def find_password(door_id):
    password = ""
    index = 0

    while len(password) < 8:
        hash_input = door_id + str(index)
        hash_result = hashlib.md5(hash_input.encode()).hexdigest()

        if hash_result.startswith("00000"):
            password += hash_result[5]
            print(f"Found character: {hash_result[5]} at index {index}")

        index += 1

    return password


door_id = "uqwqemis"
password = find_password(door_id)
print("The password is:", password)
