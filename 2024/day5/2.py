f = open("day5/data.txt", "r")
data = f.read()

data_splitted = data.split("\n\n")
rules_lines = data_splitted[0].split("\n")
update_lines = data_splitted[1].split("\n")
rules = list(map(lambda x: list(map(lambda y: int(y), x.split("|"))), rules_lines))
updates = list(map(lambda x: list(map(lambda y: int(y), x.split(","))), update_lines))

def custom_index(it, pred, default=-1):
    return next((i for i, e in enumerate(it) if pred(e)), default)

def produce_sequence(rules):
    sequence = []

    sequence.append(rules[0][0])
    sequence.append(rules[0][1])
    del rules[0]

    work_idx = len(sequence) - 1
    mode = 'append'

    while len(rules) > 0:
        if mode == 'append':
            idx = custom_index(rules, lambda x: x[0] == sequence[work_idx])

            if idx == -1:
                work_idx -= 1
                if work_idx < 0:
                    mode = 'prepend'
                    work_idx = 0
                continue
            item = rules[idx]

            if item[1] not in sequence:
                sequence.insert(work_idx + 1, item[1])
            del rules[idx]
        else:
            idx = custom_index(rules, lambda x: x[1] == sequence[work_idx])
            if idx == -1:
                work_idx += 1
                if work_idx == len(sequence):
                    mode = 'append'
                    work_idx = len(sequence) - 1
                    break
                continue
            item = rules[idx]
            if item[0] not in sequence:
                sequence.insert(work_idx , item[0])
            del rules[idx]


print(sequence)