from itertools import product

f = open("day7/data.txt", "r")
data = f.read()
lines = data.split("\n")


def process(expected_result, values: list[int], operations: list[str]):
    if len(values) == 1:
        return values[0] == expected_result

    left = values[0]
    right = values[1]

    outcome = 0
    operation = operations[0]
    if operation == "+":
        outcome = left + right
    elif operation == "*":
        outcome = left * right
    elif operation == "||":
        outcome = int(f"{left}{right}")

    values[0] = outcome
    values.pop(1)
    operations.pop(0)

    return process(expected_result, values, operations)


def check(expected_result, values):
    operation_variants = list(product(["+", "*", "||"], repeat=len(values) - 1))

    for operations in operation_variants:
        values_copy = list(values[:])
        operations_copy = list(operations[:])
        is_ok = process(expected_result, values_copy, operations_copy)
        if is_ok:
            return True
    return False


total = []

lines_length = len(lines)
idx = 0

for line in lines:
    print(f"""{idx}/{lines_length}""")
    outcome_str, values_str = line.split(": ")
    values = list(map(int, values_str.split(" ")))
    result = int(outcome_str)
    is_ok = check(result, values)
    if is_ok:
        total.append(result)
    idx += 1

print(sum(total))
