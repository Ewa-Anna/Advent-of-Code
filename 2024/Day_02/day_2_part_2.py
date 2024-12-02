from day_2_part_1 import raw_input, is_safe


def is_safe_with_removal(report):
    if is_safe(report):
        return True
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    
    return False

safe_count = sum(is_safe_with_removal(report) for report in raw_input)

print(safe_count)