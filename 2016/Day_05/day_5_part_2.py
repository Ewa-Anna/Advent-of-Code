import hashlib


def find_password(door_id):
    password = ["_"] * 8
    index = 0
    found = 0
    
    while found < 8:
        hash_input = door_id + str(index)
        hash_result = hashlib.md5(hash_input.encode()).hexdigest()
        
        if hash_result.startswith("00000"):  
            position = hash_result[5]
            char = hash_result[6]
            
            if position.isdigit():
                pos = int(position)
                if 0 <= pos < 8 and password[pos] == "_":
                    password[pos] = char
                    found += 1
                    print("Password progress:", "".join(password), end="\r", flush=True)
        
        index += 1
    
    return "".join(password)

door_id = "uqwqemis"
password = find_password(door_id)
print("\nThe password is:", password)
