f = open("day2/day2-data.txt", "r")
data = f.read()
lines = data.split("\n")

safe_report = 0


def check_sequence(line) -> bool:
    prev_value = None
    direction = None
    for current_value in line:
        if prev_value is None:
            prev_value = current_value
            continue

        diff = current_value - prev_value
        new_direction = 0
        if diff > 0:
            new_direction = 1
        elif diff < 0:
            new_direction = -1
        abs_diff = abs(diff)

        if abs_diff > 3:
            return False

        if direction is None:
            prev_value = current_value
            direction = new_direction
            continue

        if new_direction != direction:
            return False

        prev_value = current_value

    return True


def process_line(line):
    is_safe = check_sequence(line)
    if is_safe:
        return True

    for idx, current_value in enumerate(line):
        new_line = line[:idx] + line[idx + 1 :]
        is_safe = check_sequence(new_line)
        if is_safe:
            return True
    return False


for line in lines:
    int_parts = list(map(int, line.split(" ")))
    is_safe = process_line(int_parts)
    if is_safe:
        safe_report += 1
print(safe_report)
