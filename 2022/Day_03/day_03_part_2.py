from string import ascii_letters

data = "input.txt"

with open(data) as f:
    data = [line.rstrip() for line in f]

result = 0
for line in range(0, len(data), 3):
    list_1, list_2, list_3 = data[line:line+3]
    common_items_set = set(list_1).intersection(set(list_2)).intersection(set(list_3))
    common_items = common_items_set.pop()
    result += ascii_letters.index(common_items) + 1

print(result)
