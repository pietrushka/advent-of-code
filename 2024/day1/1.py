from utils.get_input import get_input

input = get_input(2024, 1)

lines = input.split("\n")
left = []
right = []
for line in lines:
    values = list(filter(lambda x: x != "", line.split(" ")))
    if len(values) != 2:
        continue
    leftValue, rightValue = values
    left.append(int(leftValue))
    right.append(int(rightValue))


left.sort()
right.sort()

total = 0
for idx, leftValue in enumerate(left):
    rightValue = right[idx]
    total += abs(leftValue - rightValue)

print(total)

