from itertools import permutations 

f = open("day7/data.txt", "r")
data = f.read()
lines = data.split("\n")

operation = ['+', '*']

# def operate (x): 

def simulate(expected_result,  values, current_result):
    if current_result == expected_result:
        return True
    if current_result > expected_result:
        return False
    

def check(expected_result, values):
    perms = list(permutations(operation, len(values) - 1))
    for perm in list(perms): 
        task = []
        for idx, val in enumerate(values):
            task.append(val)
            if idx < len(perm) :
                task.append(perm[idx])
        print(task)



total = []
for line in lines[:1]:
    outcome_str, values_str = line.split(': ')
    values = list(map(int,values_str.split(' ')))
    result = int(outcome_str)
    check(result, values)
