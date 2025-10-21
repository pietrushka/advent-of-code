import math
import sys

print(sys.getrecursionlimit())

f = open("day6/data.txt", "r")
data = f.read()
sys.setrecursionlimit(5000)


map_dict = {}
initial_current_pos = None
initial_direction = "up"
path = set()

for iy, row in enumerate(data.split("\n")):
    for ix, cell in enumerate(row):
        if cell == "^":
            initial_current_pos = (ix, iy)
            path.add(initial_current_pos)
        map_dict[(ix, iy)] = cell

size = math.sqrt(len(map_dict))  # Assume square map

print(map_dict)


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


def get_next_direction(direction):
    directions = ["up", "right", "down", "left"]
    idx = directions.index(direction)
    idx += 1
    if idx == len(directions):
        idx = 0
    return directions[idx]


def make_move(current_pos, direction):
    if check_find_exit(current_pos, direction):
        return
    next_pos = get_next_pos(current_pos=current_pos, direction=direction)
    is_next_pos_free = map_dict[next_pos] != "#"

    if is_next_pos_free:
        current_pos = next_pos
        path.add(current_pos)
        return make_move(current_pos, direction)

    new_direction = get_next_direction(direction=direction)
    return make_move(current_pos, new_direction)


make_move(initial_current_pos, initial_direction)
print(len(path))
