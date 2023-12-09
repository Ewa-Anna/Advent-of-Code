import pandas as pd

puzzle_txt = "advent_of_code_day_6_puzzle.txt"
df = pd.read_csv(puzzle_txt, sep='\s+', header=None)
num_columns = len(df.columns)
columns_to_use = list(range(1, num_columns))
df = pd.read_csv(puzzle_txt, sep='\s+', header=None,
                 usecols=columns_to_use)

# Transpose
df = df.T

result = []

# Convert strings to integers
df[0] = pd.to_numeric(df[0])
df[1] = pd.to_numeric(df[1])

# Check if v * t > s, when true: v ++ 1 and t -- 1
# E.g. Is 0 * 47 > 207? No
# E.g. Is 10 * 37 > 207? Yes

for i in range(len(df)):
    t_max = df[0].iloc[i]

    t = df[0].iloc[i]
    s = df[1].iloc[i]
    v = 0  # Starting velocity is always 0

    race = []
  
    for j in range(t_max + 1):
        if v * t > s:
            race.append(j)

        v += 1
        t -= 1

    result.append(race)

counting = 1
for race in result:
    counting *= len(race)

print(counting)
