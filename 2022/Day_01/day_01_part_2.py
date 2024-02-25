data = "input.txt"

with open(data) as f:
    data = f.read()

groups = data.strip().split("\n\n")
source = [list(map(int, group.split("\n"))) for group in groups]

output = []
for line in source:
    summa = sum(line)
    output.append(summa)
    sorterd_output = sorted(output, reverse=True)

top_3 = sorterd_output[0:3]

print(sum(top_3))
