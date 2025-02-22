import re

def decompressed_length(s):
    total_length = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            marker_match = re.match(r'\((\d+)x(\d+)\)', s[i:])
            if marker_match:
                num_chars, repeat = map(int, marker_match.groups())
                marker_len = marker_match.end()
                i += marker_len  
                total_length += num_chars * repeat
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

result = decompressed_length(data)
print("Decompressed length:", result)
