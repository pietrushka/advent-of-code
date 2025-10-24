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


def validate_trail(coordinates, end_coordinates):
    height = map_dict[coordinates]
    if height == 9:
        end_coordinates.append(coordinates)
        return end_coordinates

    neighbors = get_neighbors(coordinates)
    next_step_candidates = list(
        filter(
            lambda x: x[1] == height + 1,
            neighbors,
        ),
    )

    if len(next_step_candidates) == 0:
        return end_coordinates

    for next_step in next_step_candidates:
        validate_trail(next_step[0], end_coordinates)

    return end_coordinates


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
    end_coordinates = set(validate_trail(coordinates, []))
    total += len(end_coordinates)

print(total)
