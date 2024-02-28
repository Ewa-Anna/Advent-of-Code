from itertools import zip_longest

data = "input.txt"

input = open(data).read()

crates_data, instructions = [part.split("\n") for part in input.split("\n\n")]
crates = []
for line in crates_data:
    crate = []
    for char in line:
        if char != '[' and char != ']':
            crate.append(char)
    crates.append(crate)
crates.pop()  # Remove last row with number of crate placing


crates = ["".join(col[-2::-1]).strip() for idx,
          col in enumerate(zip_longest(*crates_data, fillvalue='')) if idx % 4 == 1]
crates = [item[::1] for item in crates]
