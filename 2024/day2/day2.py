f = open("day2-data.txt", "r")
data = f.read()
lines  = data.split("\n")

safe_report = 0

def check_sequence(line, lives=1):
    prev_value = None
    direction = None
    for idx, part in enumerate(line):
        if prev_value is None:
            prev_value = part
            continue

        diff = part - prev_value
        abs_diff = abs(diff)

        # Check if the difference is invalid
        if abs_diff > 3 or abs_diff < 1:
            if lives > 0:
                # Remove current element and retry
                new_line = line[:idx] + line[idx+1:]  # Create a copy without the current element
                return check_sequence(new_line, lives - 1)
            else:
                return False
        
        if direction is None:
            direction = 1 if diff > 0 else -1
            prev_value = part
            continue

        new_direction = 1 if diff > 0 else -1
        if new_direction != direction:
            if lives > 0:
                # Remove current element and retry
                new_line = line[:idx] + line[idx+1:]  # Create a copy without the current element
                return check_sequence(new_line, lives - 1)
            else:
                return False

        prev_value = part

    return True


for line in lines:
    int_parts = list(map(int, line.split(' ')))
    is_safe = check_sequence(int_parts)
    if is_safe:
        safe_report += 1

print(safe_report)


