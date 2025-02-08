from collections import Counter

def error_corrected_message(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    
    columns = zip(*lines)
    
    corrected_message = ''.join(Counter(col).most_common(1)[0][0] for col in columns)
    
    return corrected_message

print(error_corrected_message('input.txt'))
