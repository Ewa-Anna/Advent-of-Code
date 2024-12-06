from day_16_part_1 import parse_aunt_sues, mfcsam_results


def find_matching_sue(aunt_sues, mfcsam_results):
    for sue_id, attributes in aunt_sues.items():
        match = True
        for attr, value in attributes.items():
            if attr in mfcsam_results:
                if attr == "cats" or attr == "trees":
                    if value <= mfcsam_results[attr]:
                        match = False
                        break
                elif attr == "pomeranians" or attr == "goldfish":
                    if value >= mfcsam_results[attr]:
                        match = False
                        break
                else:
                    if value != mfcsam_results[attr]:
                        match = False
                        break
        if match:
            return sue_id
    return None

matching_sue = find_matching_sue(parse_aunt_sues("input.txt"), mfcsam_results)
print(matching_sue)