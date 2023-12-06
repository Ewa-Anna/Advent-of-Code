import pandas as pd

puzzle_txt = "advent_of_code_day_6_puzzle.txt"
df = pd.read_csv(puzzle_txt, sep='\s+', header=None)
num_columns = len(df.columns)
columns_to_use = list(range(1, num_columns))
df = pd.read_csv(puzzle_txt, sep='\s+', header=None,
                 usecols=columns_to_use)

time = ''.join(map(str, df.iloc[0]))
distance = ''.join(map(str, df.iloc[1]))

result = []

t_max = int(time)

t = int(time)
s = int(distance)
v = 0 

for j in range(t_max + 1):
    if v * t > s:
        result.append(j)

    v += 1
    t -= 1

print(len(result))