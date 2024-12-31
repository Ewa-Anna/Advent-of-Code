def evolve_secret(secret):
    for _ in range(2000):
        secret ^= (secret * 64) % 16777216
        secret %= 16777216

        secret ^= (secret // 32) % 16777216
        secret %= 16777216

        secret ^= (secret * 2048) % 16777216
        secret %= 16777216

    return secret

with open("input.txt", "r") as file:
    initial_secrets = [int(line.strip()) for line in file]

result = sum(evolve_secret(secret) for secret in initial_secrets)

print("Sum of the 2000th secret numbers:", result)
