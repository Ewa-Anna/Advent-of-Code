import hashlib

def find_advent_coin(secret_key):
    number = 1
    while True:
        input_str = secret_key + str(number)
        
        hash_result = hashlib.md5(input_str.encode()).hexdigest()
        
        if hash_result.startswith("00000"):
            return number
        
        number += 1

secret_key = "bgvyzdsv"
result = find_advent_coin(secret_key)
print(result)
