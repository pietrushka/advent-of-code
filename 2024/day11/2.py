import sys

sys.setrecursionlimit(1000000000)


stones = open("day11/data.txt", "r").read().split()


def apply_rules(stone):
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        left = str(int(stone[: (len(stone) // 2)]))
        right = str(int(stone[(len(stone) // 2) :]))
        return [left, right]
    else:
        return [str(int(stone) * 2024)]


cache = {}


def process(stone, level):
    if (stone, level) in cache:
        return cache[(stone, level)]
    if not stone:
        return 0
    if not level:
        return 1

    result = apply_rules(stone)
    left = result[0]
    right = len(result) > 1 and result[1] or None

    cache[(stone, level)] = process(left, level - 1) + process(right, level - 1)

    return cache[(stone, level)]


total = 0

for stone in stones:
    total += process(stone, 75)

print(total)
