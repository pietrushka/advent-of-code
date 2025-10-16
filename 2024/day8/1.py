f = open("day8/data.txt", "r")
data = f.read()

lines = data.split("\n")
x_size = len(lines[0])
y_size = len(lines)

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
    for base_location in locations:
        for other_location in locations:
            if base_location == other_location:
                continue

            x_vector = other_location[0] - base_location[0]
            y_vector = other_location[1] - base_location[1]

            x_antinode = other_location[0] + x_vector
            y_antinode = other_location[1] + y_vector
            if (
                x_antinode < 0
                or x_antinode >= x_size
                or y_antinode < 0
                or y_antinode >= y_size
            ):
                continue
            antinode = f"{x_antinode},{y_antinode}"

            antinodes.add(antinode)

print(antinodes)
print(len(antinodes))
