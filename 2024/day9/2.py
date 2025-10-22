import sys

f = open("day9/data.txt", "r")
data = f.read()

sys.setrecursionlimit(500000)

disk = []

id = 0
for idx, file in enumerate(data):
    is_empty = idx % 2 == 1

    for i in range(int(file)):
        if is_empty:
            disk.append(".")
        else:
            disk.append(id)

    if not is_empty:
        id += 1


def find_gap(disk, size, rightIdx):
    gap_start_idx = None

    for idx in range(0, rightIdx):
        if disk[idx] != ".":
            if gap_start_idx is not None:
                gap_start_idx = None

        if disk[idx] == ".":
            if gap_start_idx is None:
                gap_start_idx = idx

            if idx - gap_start_idx == size - 1:
                return gap_start_idx


def process(disk, rightIdx):
    if rightIdx % 10 == 0:
        print(rightIdx)

    if rightIdx < 1:
        return disk

    if disk[rightIdx] == ".":
        return process(disk, rightIdx - 1)

    right_file_size = 0
    value = disk[rightIdx]
    while disk[rightIdx - right_file_size] == value:
        right_file_size += 1

    gap_idx = find_gap(disk, right_file_size, rightIdx)

    if not gap_idx:
        return process(disk, rightIdx - right_file_size)

    for i in range(right_file_size):
        disk[gap_idx + i] = value

    for i in range(right_file_size):
        disk[rightIdx - i] = "."

    return process(disk, rightIdx - right_file_size)


print(process(disk, len(disk) - 1))

total = 0
for idx, x in enumerate(disk):
    if x == ".":
        continue
    total += idx * x

print("total", total)
