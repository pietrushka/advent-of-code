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

right_count_map = {}
for right_value in right: 
    if right_value in right_count_map:
        right_count_map[right_value] += 1
    else:
        right_count_map[right_value] = 1

total = 0
for left_value in left:
    count = right_count_map.get(left_value, 0)
    total += left_value * count

print(total)