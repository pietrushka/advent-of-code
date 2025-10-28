# task kinda missleading

data = open("day13/data.txt", "r").read().split("\n\n")

machines = []

a_cost = 3
b_cost = 1
max_press = 100

for block in data:
    details = block.split("\n")
    button_a = list(
        map(
            lambda x: int(x.split("+")[1]),
            details[0].split(": ")[1].split(", "),
        )
    )
    button_b = list(
        map(
            lambda x: int(x.split("+")[1]),
            details[1].split(": ")[1].split(", "),
        )
    )
    prize = list(
        map(
            lambda x: int(x.split("=")[1]) + 10000000000000,
            details[2].split(": ")[1].split(", "),
        )
    )
    machines.append((button_a, button_b, prize))


def solve(button_a, button_b, prize):
    # x * button_a + y * button_b = prize
    # x * button_a[0] + y * button_b[0] = prize[0]
    # x * button_a[1] + y * button_b[1] = prize[1]

    a1 = button_a[0]
    b1 = button_b[0]
    c1 = prize[0]

    a2 = button_a[1]
    b2 = button_b[1]
    c2 = prize[1]

    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    if D == 0:
        return None

    # integer solutions only
    if Dx % D != 0 or Dy % D != 0:
        return None

    x = Dx // D
    y = Dy // D

    return (x, y) if x > 0 and y > 0 else None


total_tokens_spent = 0

for machine in machines:
    (a_button, b_button, prize) = machine
    outcome = solve(a_button, b_button, prize)
    if outcome is None:
        continue

    total_tokens_spent += outcome[0] * a_cost + outcome[1] * b_cost


print(total_tokens_spent)
