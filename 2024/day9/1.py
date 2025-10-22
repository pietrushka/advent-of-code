f = open("day9/data.txt", "r")
data = f.read()

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

# print(disk)


for x in range(len(disk) - 1, -1, -1):
    print(x)
    val = disk[x]
    if val == ".":
        continue

    for y in range(0, x):
        if disk[y] == ".":
            disk[y] = val
            disk[x] = "."
            break

# print(disk)


total = 0
for idx, x in enumerate(disk):
    if x == ".":
        break
    total += idx * x

print("total", total)
