data = open("day14/data.txt", "r").read().split("\n")

max_x = 101
max_y = 103

robots = []
for line in data:
    posString, velString = line.split(" ")
    position = list(map(lambda x: int(x), posString.split("=")[1].split(",")))
    velocity = list(map(lambda x: int(x), velString.split("=")[1].split(",")))
    robots.append([position, velocity])


for second in range(100):
    for robot in robots:
        (x, y), (vx, vy) = robot

        x = (x + vx) % max_x
        y = (y + vy) % max_y
        robot[0] = [x, y]

quarters = [
    0,
    0,
    0,
    0,
]

middle_x = max_x // 2
middle_y = max_y // 2


for robot in robots:
    (x, y) = robot[0]
    if x == middle_x or y == middle_y:
        continue
    if x < middle_x and y < middle_y:
        quarters[0] += 1
    elif x < middle_x and y > middle_y:
        quarters[1] += 1
    elif x > middle_x and y < middle_y:
        quarters[2] += 1
    elif x > middle_x and y > middle_y:
        quarters[3] += 1

print(quarters[0] * quarters[1] * quarters[2] * quarters[3])
