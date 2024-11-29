def increment_password(password):
    password = list(password)  
    i = len(password) - 1  
    
    while i >= 0:
        if password[i] == 'z':
            password[i] = 'a'
            i -= 1  
        else:
            password[i] = chr(ord(password[i]) + 1)  
            break
    
    return ''.join(password)


def has_increasing_straight(password):
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i + 1]) + 1 == ord(password[i + 2]):
            return True
    return False


def has_no_invalid_characters(password):
    return all(c not in password for c in "iol")


def has_two_non_overlapping_pairs(password):
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 2 
        else:
            i += 1
    return len(pairs) >= 2


def is_valid_password(password):
    return (has_increasing_straight(password) and
            has_no_invalid_characters(password) and
            has_two_non_overlapping_pairs(password))


def find_next_password(current_password):
    while True:
        current_password = increment_password(current_password)
        if is_valid_password(current_password):
            return current_password


current_password = "cqjxjnds"

next_password = find_next_password(current_password)
print(next_password)
