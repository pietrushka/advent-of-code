f = open("day4/data.txt", "r")
data = f.read()

lines  = data.split("\n")

matrix = []
for line in lines:
    matrix.append(list(line))

total = 0

def safe_idx(arr, idx):
    try:
        return arr[idx]
    except IndexError:
        return None
    
def safe_idx_matrix(matrix, idx1, idx2):
    if idx1 < 0 or idx2 < 0:
        return None
    try:
        return matrix[idx1][idx2]
    except IndexError:
        return None
    
for row_idx, row in enumerate(matrix):
    for col_idx, char in enumerate(row):
        if char != 'A':
            continue

        # right = [safe_idx(row, col_idx + 1), safe_idx(row, col_idx + 2), safe_idx(row, col_idx + 3)]
        # left = [safe_idx(row, col_idx - 1), safe_idx(row, col_idx - 2), safe_idx(row, col_idx - 3)]
        # down = [safe_idx_matrix(matrix, row_idx + 1, col_idx), safe_idx_matrix(matrix, row_idx + 2, col_idx), safe_idx_matrix(matrix, row_idx + 3, col_idx)]
        # up = [safe_idx_matrix(matrix, row_idx - 1, col_idx), safe_idx_matrix(matrix, row_idx - 2, col_idx), safe_idx_matrix(matrix, row_idx - 3, col_idx)]
        up_right =safe_idx_matrix(matrix, row_idx -1, col_idx + 1)
        up_left = safe_idx_matrix(matrix, row_idx -1, col_idx - 1)
        down_right = safe_idx_matrix(matrix, row_idx + 1, col_idx + 1)
        down_left = safe_idx_matrix(matrix, row_idx + 1, col_idx - 1)
        x1 = [up_left, down_right]
        x2 = [up_right, down_left]

        if 'M' in x1 and 'M' in x2 and 'S' in x1 and 'S' in x2:
            total += 1

print(total)