def safe_get_index(arr, value):
    try:
        return arr.index(value)
    except ValueError:
        return None

def validate_update(update, rules):
    """
    Validate if an update satisfies the ordering rules.
    """
    for x, y in rules:
        first_idx = safe_get_index(update, x)
        second_idx = safe_get_index(update, y)
        if first_idx is not None and second_idx is not None and first_idx > second_idx:
            return False
    return True

def get_middle(arr):
    """
    Get the middle value of an array.
    """
    print(arr)
    return arr[len(arr) // 2]

def produce_sequence(rules):
    """
    Produce a valid sequence of page numbers based on the ordering rules.
    """
    from collections import defaultdict, deque

    # Build graph and in-degree count for topological sort
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    pages = set()
    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        pages.add(x)
        pages.add(y)

    # Find nodes with no incoming edges
    queue = deque([node for node in pages if in_degree[node] == 0])
    sequence = []

    while queue:
        current = queue.popleft()
        sequence.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sequence

def correct_sequence(update, sequence):
    """
    Correct an update's order based on the produced valid sequence.
    """
    return [page for page in sequence if page in update]

# Load data
with open("day5/data.txt", "r") as f:
    data = f.read()

data_splitted = data.split("\n\n")
rules_lines = data_splitted[0].split("\n")
update_lines = data_splitted[1].split("\n")

# Parse rules and updates
rules = [list(map(int, line.split("|"))) for line in rules_lines]
updates = [list(map(int, line.split(","))) for line in update_lines]

# Generate valid sequence
sequence = produce_sequence(rules)
print('Valid Sequence:', sequence)

# Calculate the total from corrected updates
total = 0
for update in updates:
    if validate_update(update, rules):
        continue  # Skip valid updates

    corrected_update = correct_sequence(update, sequence)
    print('Corrected Update:', corrected_update)
    middle_value = get_middle(corrected_update)
    print('Middle Value:', middle_value)
    total += middle_value

print('Total:', total)
