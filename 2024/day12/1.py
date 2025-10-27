data = open("day12/data.txt", "r").read().split("\n")

map = {}

max_x = None
max_y = len(data) - 1

for y_idx, line in enumerate(data):
    if max_x is None:
        max_x = len(line) - 1
    for x_idx, char in enumerate(line):
        map[(x_idx, y_idx)] = [char, False]


def get_neighbours(init_x, init_y, value):
    positions = [
        (init_x + 1, init_y),
        (init_x - 1, init_y),
        (init_x, init_y + 1),
        (init_x, init_y - 1),
    ]
    new_neighbours = []
    all_neighbours_count = 0
    for x, y in positions:
        if x >= 0 and x <= max_x and y >= 0 and y <= max_y:
            if map[(x, y)][0] == value:
                all_neighbours_count += 1
                if not map[(x, y)][1]:
                    new_neighbours.append((x, y))
    return (new_neighbours, all_neighbours_count)


def process(x, y, value):
    map[(x, y)][1] = True

    (neighbours, all_neighbours_count) = get_neighbours(x, y, value)

    area = 1
    perimiter = 4 - all_neighbours_count

    for neighbour_x, neighbour_y in neighbours:
        map[(neighbour_x, neighbour_y)][1] = True

    for neighbour_x, neighbour_y in neighbours:
        (neighbour_area, neighbour_perimiter) = process(neighbour_x, neighbour_y, value)
        area += neighbour_area
        perimiter += neighbour_perimiter

    return (area, perimiter)


fence = 0

for x, y in map:
    (value, visited) = map[(x, y)]
    if visited:
        continue
    (area, perimiter) = process(x, y, value)
    fence += area * perimiter

print(fence)
