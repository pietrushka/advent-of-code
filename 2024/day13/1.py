data = open("day13/data.txt", "r").read().split("\n\n")

machines = []

a_cost = 3
b_cost = 1
max_press = 100

for block in data:
    details = block.split("\n")
    button_a = list(
        map(lambda x: int(x.split("+")[1]), details[0].split(": ")[1].split(", "))
    )
    button_b = list(
        map(lambda x: int(x.split("+")[1]), details[1].split(": ")[1].split(", "))
    )
    prize = list(
        map(lambda x: int(x.split("=")[1]), details[2].split(": ")[1].split(", "))
    )
    machines.append((button_a, button_b, prize))


def simulate(a_press, b_press, button_a, button_b, prize):
    a_move = (button_a[0] * a_press, button_a[1] * a_press)
    b_move = (button_b[0] * b_press, button_b[1] * b_press)
    x = a_move[0] + b_move[0]
    y = a_move[1] + b_move[1]

    if x != prize[0] or y != prize[1]:
        return False
    return (a_press * a_cost) + (b_press * b_cost)


total_tokens_spent = 0

for machine in machines:
    tokens = None
    for a_press in range(1, max_press + 1):
        for b_press in range(1, max_press + 1):
            trial_tokens = simulate(a_press, b_press, *machine)
            if not trial_tokens or (tokens is not None and trial_tokens > tokens):
                continue
            tokens = trial_tokens
    if tokens is None:
        continue
    total_tokens_spent += tokens


print(total_tokens_spent)
