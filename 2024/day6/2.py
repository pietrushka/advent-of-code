import math
import sys

# print(sys.getrecursionlimit())

f = open("day6/data'.txt", "r")
data = f.read()
sys.setrecursionlimit(10000)


initial_map_dict = {}
initial_current_pos = None
initial_direction = "up"

for iy, row in enumerate(data.split("\n")):
    for ix, cell in enumerate(row):
        if cell == "^":
            initial_current_pos = (ix, iy)
        initial_map_dict[(ix, iy)] = cell

size = math.sqrt(len(initial_map_dict))  # Assume square map


def get_next_pos(current_pos, direction):
    if direction == "up":
        return (current_pos[0], current_pos[1] - 1)
    elif direction == "down":
        return (current_pos[0], current_pos[1] + 1)
    elif direction == "left":
        return (current_pos[0] - 1, current_pos[1])
    elif direction == "right":
        return (current_pos[0] + 1, current_pos[1])
    else:
        raise Exception("Invalid direction")


def get_next_direction(direction):
    directions = ["up", "right", "down", "left"]
    idx = directions.index(direction)
    idx += 1
    if idx == len(directions):
        idx = 0
    return directions[idx]


def check_find_exit(current_pos, direction):
    (x, y) = current_pos

    if direction == "up" and y == 0:
        return True
    elif direction == "down" and y == size - 1:
        return True
    elif direction == "left" and x == 0:
        return True
    elif direction == "right" and x == size - 1:
        return True

    return False


def simulate_path(map_dict, current_pos, direction, path):
    if check_find_exit(current_pos, direction):
        return False

    next_pos = get_next_pos(current_pos=current_pos, direction=direction)
    is_next_pos_free = map_dict[next_pos] != "#"

    if is_next_pos_free:
        if (next_pos, direction) in path:
            return True
        path.add((next_pos, direction))
        return simulate_path(map_dict, next_pos, direction, path)

    new_direction = get_next_direction(direction=direction)
    return simulate_path(map_dict, current_pos, new_direction, path)


total = 0
total_length = len(initial_map_dict.items())
idx = 1

for item in list(initial_map_dict.items()):
    print(f"{idx}/{total_length}")
    map_dict_copy = initial_map_dict.copy()
    item_value = item[1]
    if item_value == "#" or item_value == "^":
        continue

    item_x = item[0][0]
    item_y = item[0][1]

    map_dict_copy[item_x, item_y] = "#"

    path = set()

    result = simulate_path(
        map_dict_copy,
        current_pos=initial_current_pos,
        direction=initial_direction,
        path=path,
    )

    if result:
        total += 1

    idx += 1

print(total)
