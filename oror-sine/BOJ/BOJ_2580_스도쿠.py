import sys
sudoku = [[0]*9 for _ in range(9)]
needed_rows = [[True for _ in range(9)] for _ in range(9)]
needed_cols = [[True for _ in range(9)] for _ in range(9)]
needed_boxes = [[[True for _ in range(9)] for _ in range(3)]for _ in range(3)]
needed = []
for r in range(9):
    for c, cell in enumerate(sys.stdin.readline().split()):
        if num := int(cell):
            num_idx = num - 1
            needed_rows[r][num_idx] = False
            needed_cols[c][num_idx] = False
            needed_boxes[r//3][c//3][num_idx] = False
            sudoku[r][c] = num
        else:
            needed.append((r, c))

possible_num_idxs = [[] for _ in range(len(needed))]
for idx, coord in enumerate(needed):
    r, c = coord
    for num_idx in range(9):
        if needed_rows[r][num_idx] and needed_cols[c][num_idx] and needed_boxes[r//3][c//3][num_idx]:
            possible_num_idxs[idx].append(num_idx)

def backtrack(i):
    if i == len(needed):
        return True
    r, c = needed[i]
    for num_idx in possible_num_idxs[i]:
        if needed_rows[r][num_idx] and needed_cols[c][num_idx] and needed_boxes[r//3][c//3][num_idx]:
            needed_rows[r][num_idx] = False
            needed_cols[c][num_idx] = False
            needed_boxes[r//3][c//3][num_idx] = False
            sudoku[r][c] = num_idx + 1
            if backtrack(i+1):
                return True
            needed_rows[r][num_idx] = True
            needed_cols[c][num_idx] = True
            needed_boxes[r//3][c//3][num_idx] = True
            sudoku[r][c] = 0
    return False

backtrack(0)
for row in sudoku:
    print(*row)
