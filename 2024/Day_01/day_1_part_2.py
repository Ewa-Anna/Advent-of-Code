from collections import Counter
from day_1_part_1 import right_column, left_column

right_counts = Counter(right_column)

similarity_score = 0
for num in left_column:
    count_in_right = right_counts.get(num, 0) 
    similarity_score += num * count_in_right

print(similarity_score)