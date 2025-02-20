import math
import sys
sys.setrecursionlimit(10000)

f = open("day6/data.txt", "r")
data = f.read()


map_dict = {}
initial_pos = None
initial_direction = 'up'
path = set()
path_arr = []
possible_loops = set()

for iy, row in enumerate(data.split("\n")):
    for ix, cell in enumerate(row): 
        if cell == '^':
            initial_pos = (ix, iy)
            path.add((ix, iy, initial_direction))
            path_arr.append((ix, iy, initial_direction))
        map_dict[(ix, iy)] = cell

size = math.sqrt(len(map_dict))  # Assume square map

def get_next_pos(current_pos, direction):
    if direction == 'up':
        return (current_pos[0], current_pos[1] - 1)
    elif direction == 'down':
        return (current_pos[0], current_pos[1] + 1)
    elif direction == 'left':
        return (current_pos[0] - 1, current_pos[1])
    elif direction == 'right':
        return (current_pos[0] + 1, current_pos[1])
    else:
        raise Exception('Invalid direction')

def check_find_exit(current_pos, direction):
    (x, y) = current_pos

    if direction == 'up' and y == 0:
        return True
    elif direction == 'down' and y == size - 1:
        return True
    elif direction == 'left' and x == 0:
        return True
    elif direction == 'right' and x == size - 1:
        return True

    return False
    
def get_next_direction(direction):
    directions = ['up', 'right', 'down', 'left']
    idx = directions.index(direction)
    idx += 1
    if idx == len(directions):
        idx = 0
    return directions[idx]

def check_loop(current_pos, direction):
    temp_path = path.copy()
    next_direction = get_next_direction(direction=direction)
    block_position = get_next_pos(current_pos=current_pos, direction=direction)
    is_loop = simulate_moves(current_pos=current_pos, direction=next_direction, temp_path=temp_path, block_position=block_position)
    return is_loop

def simulate_moves(current_pos, direction, temp_path, block_position):
    if check_find_exit(current_pos, direction):
        return False

    next_pos = get_next_pos(current_pos=current_pos, direction=direction)

    if (next_pos[0], next_pos[1], direction) in temp_path:
        return True
    
    is_next_pos_free = map_dict[next_pos] != '#' and next_pos != block_position

    if is_next_pos_free:
        current_pos = next_pos
        temp_path.add((next_pos[0], next_pos[1], direction))
        return simulate_moves(current_pos=current_pos, direction=direction, temp_path=temp_path, block_position=block_position)

    new_direction = get_next_direction(direction=direction)
    temp_path.add((current_pos[0], current_pos[1], new_direction))

    return simulate_moves(current_pos, new_direction, temp_path, block_position=block_position)

def make_move(current_pos, direction):
    if check_find_exit(current_pos, direction):
        return
    next_pos = get_next_pos(current_pos=current_pos, direction=direction)
    is_next_pos_free = map_dict[next_pos] != '#'

    if is_next_pos_free:
        if len(path) > 1 and check_loop(current_pos=current_pos, direction=direction):
            possible_loops.add(next_pos)
        current_pos = next_pos
        path.add((next_pos[0], next_pos[1], direction))
        path_arr.append((next_pos[0], next_pos[1], direction))
        return make_move(current_pos, direction)

    new_direction = get_next_direction(direction=direction)
    path.add((current_pos[0], current_pos[1], new_direction))
    path_arr.append((current_pos[0], current_pos[1], new_direction))

    return make_move(current_pos, new_direction)

make_move(initial_pos, initial_direction)
print(possible_loops)
print(len(possible_loops))