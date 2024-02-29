data = "input.txt"

with open(data) as f:
    data = [line.rstrip() for line in f]

DIGITS = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}

total = 0
for line in data:
    N = 0
    for char in line:
        N *= 5
        N += DIGITS[char]
    total += N


def f(n):
    if n == 0:
        return []
    if (n % 5) == 0:
        return ["0"] + f(n // 5)
    if (n % 5) == 1:
        return ["1"] + f(n // 5)
    if (n % 5) == 2:
        return ["2"] + f(n // 5)
    if (n % 5) == 3:
        return ["="] + f((n + 2) // 5)
    if (n % 5) == 4:
        return ["-"] + f((n + 1) // 5)


print("".join(f(total)[::-1]))
