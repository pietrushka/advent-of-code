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
    for x, y in positions:
        if x >= 0 and x <= max_x and y >= 0 and y <= max_y:
            if map[(x, y)][0] == value:
                if not map[(x, y)][1]:
                    new_neighbours.append((x, y))
    return new_neighbours


def get_all_neighbours(init_x, init_y, value):
    left = (
        (init_x - 1, init_y)
        if init_x > 0 and map[(init_x - 1, init_y)][0] == value
        else None
    )
    right = (
        (init_x + 1, init_y)
        if init_x < max_x and map[(init_x + 1, init_y)][0] == value
        else None
    )
    up = (
        (init_x, init_y - 1)
        if init_y > 0 and map[(init_x, init_y - 1)][0] == value
        else None
    )
    down = (
        (init_x, init_y + 1)
        if init_y < max_y and map[(init_x, init_y + 1)][0] == value
        else None
    )
    return (left, right, up, down)


def process(
    x,
    y,
    value,
):
    map[(x, y)][1] = True

    new_neighbours = get_neighbours(x, y, value)
    (left, right, up, down) = get_all_neighbours(x, y, value)

    sides = []

    if not left:
        sides.append(((x, y), (x, y + 1), "v", "l"))
    if not right:
        sides.append(((x + 1, y), (x + 1, y + 1), "v", "r"))
    if not up:
        sides.append(((x, y), (x + 1, y), "h", "t"))
    if not down:
        sides.append(((x, y + 1), (x + 1, y + 1), "h", "d"))

    area = 1
    for neighbour_x, neighbour_y in new_neighbours:
        map[(neighbour_x, neighbour_y)][1] = True

    for neighbour_x, neighbour_y in new_neighbours:
        (neighbour_area, neighbour_sides) = process(neighbour_x, neighbour_y, value)
        area += neighbour_area
        sides.extend(neighbour_sides)
    return (area, sides)


def process_side(left, right, orientation, area_side, sides, walls):
    for idx, side in enumerate(sides):
        if side[1] == left and orientation == side[2] and side[3] == area_side:
            sides.pop(idx)
            return process_side(side[0], right, orientation, area_side, sides, walls)
        if side[0] == right and orientation == side[2] and side[3] == area_side:
            sides.pop(idx)
            return process_side(left, side[1], orientation, area_side, sides, walls)

    if len(sides) == 0:
        return walls

    (new_left, new_right, new_orientation, new_area_side) = sides.pop()
    walls += 1
    return process_side(
        new_left, new_right, new_orientation, new_area_side, sides, walls
    )


fence = 0

for x, y in map:
    (value, visited) = map[(x, y)]
    if visited:
        continue
    (area, sides) = process(
        x,
        y,
        value,
    )

    (new_left, new_right, new_orientation, area_side) = sides.pop()
    walls = process_side(new_left, new_right, new_orientation, area_side, sides, 1)
    fence += area * walls


print(fence)
