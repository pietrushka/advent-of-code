f = open("day8/data.txt", "r")
data = f.read()

lines = data.split("\n")
x_boundary = len(lines[0]) - 1
y_boundry = len(lines) - 1

antenas_locations = {}
for line_idx, line in enumerate(lines):
    for char_idx, char in enumerate(line):
        if char == ".":
            continue

        if char not in antenas_locations:
            antenas_locations[char] = []

        antenas_locations[char].append([char_idx, line_idx])

antinodes = set()

for antenna, locations in antenas_locations.items():
    antenas_count = len(locations)
    for base_location in locations:
        for other_location in locations:
            if base_location == other_location:
                continue
            antena_antinode = f"{other_location[0]},{other_location[1]}"
            antinodes.add(antena_antinode)

            x_vector = other_location[0] - base_location[0]
            y_vector = other_location[1] - base_location[1]

            exceeds_boundary = False
            multiplier = 1
            while not exceeds_boundary:
                x_vector_mod = x_vector * multiplier
                y_vector_mod = y_vector * multiplier

                x_antinode = other_location[0] + x_vector_mod
                y_antinode = other_location[1] + y_vector_mod
                if (
                    x_antinode < 0
                    or x_antinode > x_boundary
                    or y_antinode < 0
                    or y_antinode > y_boundry
                ):
                    break

                antinode = f"{x_antinode},{y_antinode}"
                antinodes.add(antinode)
                multiplier += 1


print(antinodes)
print(len(antinodes))
