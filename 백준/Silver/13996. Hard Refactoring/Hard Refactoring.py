import sys

def preprocess():
    ranges = []

    for line in sys.stdin:
        line = line.strip().replace("||", "").split("&&")
        if len(line) == 1:
            comp, value = line[0].split("=")
            value = int(value)
            if ">" in comp:
                ranges.append([value, 32767])
            else:
                ranges.append([-32768, value])
        else:
            low, high = int(line[0].split("=")[1]), int(line[1].split("=")[1])
            if low <= high:
                ranges.append([low, high])

    return merge_ranges(ranges)

def merge_ranges(ranges):
    if not ranges:
        return []

    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]

    for current in sorted_ranges[1:]:
        prev_high = merged[-1][1]

        if current[0] <= prev_high + 1:
            merged[-1][1] = max(prev_high, current[1])
        else:
            merged.append(current)

    return merged

def format_ranges(ranges):
    if not ranges:
        return "false"

    if ranges[0][0] == -32768 and ranges[0][1] == 32767:
        return "true"

    result = []
    for start, end in ranges:
        if start == -32768:
            result.append(f"x <= {end}")
        elif end == 32767:
            result.append(f"x >= {start}")
        else:
            result.append(f"x >= {start} && x <= {end}")

    return " ||\n".join(result)

if __name__ == "__main__":
    ranges = preprocess()
    print(format_ranges(ranges))