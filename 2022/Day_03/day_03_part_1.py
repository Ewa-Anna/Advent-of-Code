from string import ascii_letters

data = "input.txt"

with open(data) as f:
    data = [line.rstrip() for line in f]

result = 0
for line in data:
    amount = len(line)
    position = int(amount // 2)
    list_1 = line[:position]
    list_2 = line[position:]
    common_items_set = set(list_1).intersection(list_2)
    common_items = common_items_set.pop()
    result += ascii_letters.index(common_items) + 1

print(result)
