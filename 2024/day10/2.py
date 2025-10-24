f = open("day10/data.txt", "r")
data = f.read()


max_x = 0
max_y = 0
map_dict = {}
heads = []


def get_neighbors(coordinates):
    (x, y) = coordinates
    return list(
        filter(
            lambda x: x is not None,
            [
                ((x - 1, y), map_dict[x - 1, y]) if x > 0 else None,
                ((x + 1, y), map_dict[x + 1, y]) if x < max_x else None,
                ((x, y - 1), map_dict[x, y - 1]) if y > 0 else None,
                ((x, y + 1), map_dict[x, y + 1]) if y < max_y else None,
            ],
        )
    )


def validate_trail(coordinates, current_trail, all_trails):
    height = map_dict[coordinates]
    if height == 9:
        current_trail.append(coordinates)
        all_trails.append(current_trail)
        return all_trails

    neighbors = get_neighbors(coordinates)
    next_step_candidates = list(
        filter(
            lambda x: x[1] == height + 1,
            neighbors,
        ),
    )

    if len(next_step_candidates) == 0:
        return all_trails

    for next_step in next_step_candidates:
        trail_copy = current_trail.copy()
        trail_copy.append(next_step[0])
        validate_trail(next_step[0], trail_copy, all_trails)

    return all_trails


for iy, row in enumerate(data.split("\n")):
    if iy > max_y:
        max_y = iy
    for ix, cell in enumerate(row):
        if ix > max_x:
            max_x = ix
        map_dict[(ix, iy)] = int(cell)

total = 0

for [coordinates, height] in map_dict.items():
    if height != 0:
        continue
    trails = validate_trail(coordinates, [coordinates], [])
    trails_strs = list(map(lambda x: str(x), trails))
    total += len(set(trails_strs))

print(total)
