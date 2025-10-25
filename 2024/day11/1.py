import sys
from multiprocessing import Pool, cpu_count

f = open("day11/data.txt", "r")
data = f.read()

sys.setrecursionlimit(1000000)

stones = list(map(lambda x: int(x), data.split(" ")))

blinks = 25


def apply_rules(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_string = str(stone)
        stone_number_digit_count = len(stone_string)
        left = int(stone_string[: (stone_number_digit_count // 2)])
        right = int(stone_string[(stone_number_digit_count // 2) :])
        return [left, right]
    else:
        return [int(stone) * 2024]


def process(idx, stone_list):
    if idx > len(stone_list) - 1:
        return stone_list
    stone = stone_list[idx]
    updated = apply_rules(stone)
    stone_list[idx : idx + 1] = updated
    return process(idx + len(updated), stone_list)


def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def work(chunk):
    return process(0, list(chunk))


cpus = cpu_count()

for i in range(blinks):
    print("blink:", i, len(stones))
    size = max(1, len(stones) // cpus)
    chunks = list(chunk_list(stones, size))

    with Pool(cpus) as pool:
        results = pool.map(work, chunks)

    stones = []
    for result in results:
        stones.extend(result)

print("final:", len(stones))
