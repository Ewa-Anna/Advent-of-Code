import re

def decompressed_length_v2(s, start=0, end=None):
    if end is None:
        end = len(s)
    
    total_length = 0
    i = start

    while i < end:
        if s[i] == '(':
            marker_match = re.match(r'\((\d+)x(\d+)\)', s[i:])
            if marker_match:
                num_chars, repeat = map(int, marker_match.groups())
                marker_len = marker_match.end()
                i += marker_len 

                segment_length = decompressed_length_v2(s, i, i + num_chars)
                total_length += segment_length * repeat
                i += num_chars 
            else:
                total_length += 1
                i += 1
        elif s[i].isspace():
            i += 1 
        else:
            total_length += 1
            i += 1

    return total_length

with open('input.txt', 'r') as file:
    data = file.read().strip()

result = decompressed_length_v2(data)
print("Decompressed length (v2):", result)
