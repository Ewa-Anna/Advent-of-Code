import re
from day_3_part_1 import corrupted_memory


mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

enabled = True
total_sum = 0

for match in re.finditer(f"{do_pattern}|{dont_pattern}|{mul_pattern}", corrupted_memory):
    instruction = match.group()
    
    if re.fullmatch(do_pattern, instruction):
        enabled = True
    elif re.fullmatch(dont_pattern, instruction):
        enabled = False
    elif enabled and re.fullmatch(mul_pattern, instruction):
        x, y = map(int, re.findall(r"\d+", instruction))
        total_sum += x * y

print(total_sum)