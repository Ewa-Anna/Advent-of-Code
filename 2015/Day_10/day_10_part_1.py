def look_and_say(sequence, iterations): 
    for _ in range(iterations):
        result = []
        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                count += 1
            else:
                result.append(f"{count}{sequence[i - 1]}")
                count = 1
        result.append(f"{count}{sequence[-1]}")
        sequence = ''.join(result)
    return sequence

puzzle_input = "1113222113"

result_sequence = look_and_say(puzzle_input, 40)

print(len(result_sequence))
