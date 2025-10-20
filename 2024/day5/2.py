f = open("day5/data.txt", "r")
data = f.read()

data_splitted = data.split("\n\n")
rules_lines = data_splitted[0].split("\n")
update_lines = data_splitted[1].split("\n")
rules = list(map(lambda x: list(map(lambda y: int(y), x.split("|"))), rules_lines))
updates = list(map(lambda x: list(map(lambda y: int(y), x.split(","))), update_lines))


def safe_get_index(arr, value):
    try:
        return arr.index(value)
    except ValueError:
        return None


def validate_update(update, rules):
    for x, y in rules:
        first_idx = safe_get_index(update, x)
        second_idx = safe_get_index(update, y)
        if first_idx is not None and second_idx is not None and first_idx > second_idx:
            print("x", x, "y", y, "first_idx", first_idx, "second_idx", second_idx)
            return False
    return True


incorrect_updates = []
for update in updates:
    if not validate_update(update, rules):
        incorrect_updates.append(update)


def order_update(update, rules):
    new_order = [update[0]]

    for num in update[1:]:
        for idx in range(len(new_order) + 1):
            temp_order = new_order[:]
            temp_order.insert(idx, num)
            is_valid = validate_update(temp_order, rules)
            if is_valid:
                new_order = temp_order
                break

    return new_order


def get_middle(arr):
    return arr[len(arr) // 2]


sum = 0

for update in incorrect_updates:
    ordered_updates = order_update(update, rules)
    sum += get_middle(ordered_updates)

print(sum)
