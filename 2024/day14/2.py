data = open("day14/data.txt", "r").read().split("\n")

max_x = 101
max_y = 103

robots = []
for line in data:
    posString, velString = line.split(" ")
    position = list(map(lambda x: int(x), posString.split("=")[1].split(",")))
    velocity = list(map(lambda x: int(x), velString.split("=")[1].split(",")))
    robots.append([position, velocity])


def validate_shape():
    scat = 0
    for robot in robots:
        (x, y) = robot[0]

        neighbours_count = 0
        for r in robots:
            (rx, ry) = r[0]
            if rx == x and ry == y:
                continue
            top = x == rx and y - 1 == ry
            bottom = x == rx and y + 1 == ry
            left = x - 1 == rx and y == ry
            right = x + 1 == rx and y == ry
            top_right = x - 1 == rx and y - 1 == ry
            bottom_right = x - 1 == rx and y + 1 == ry
            bottom_left = x + 1 == rx and y + 1 == ry
            top_left = x + 1 == rx and y - 1 == ry
            if (
                top
                or bottom
                or left
                or right
                or top_right
                or bottom_right
                or bottom_left
                or top_left
            ):
                neighbours_count += 1

        if neighbours_count < 1:
            scat += 1

    return scat < 20, scat


idx = 0
min_scat = 500


def paint():
    matrix = [[0 for _ in range(max_y)] for _ in range(max_x)]
    for robot in robots:
        (x, y) = robot[0]
        matrix[x][y] += 1
    for y in matrix:
        line = ""
        for val in y:
            if val > 0:
                line += "#"
            else:
                line += " "
        print("|" + line + "|")


while True:
    idx += 1
    if idx % 100 == 0:
        print(idx)
    for robot in robots:
        (x, y), (vx, vy) = robot

        x = (x + vx) % max_x
        y = (y + vy) % max_y
        robot[0] = [x, y]

    if idx < 7000:
        continue
    is_valid, scat = validate_shape()
    if scat < min_scat:
        min_scat = scat
        print(idx)
        print("min_scat", min_scat)
        paint()
    if is_valid:
        break


paint()
