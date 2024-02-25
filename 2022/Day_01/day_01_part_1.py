data = "input.txt"

with open(data) as f:
    data = f.read()

groups = data.strip().split("\n\n")
source = [list(map(int, group.split("\n"))) for group in groups]

output = []
for line in source:
    summa = sum(line)
    output.append(summa)
    maximum = max(output)


print(maximum)
