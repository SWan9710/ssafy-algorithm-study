grid = [[int(i) for i in input().split()] for _ in range(10)]
r = c = 1

while 1:
    if grid[r][c] == 2:
        grid[r][c] = 9
        break

    grid[r][c] = 9

    if grid[r][c + 1] != 1:
        c += 1
    elif grid[r + 1][c] != 1:
        r += 1
    else:
        break

for row in grid:
    print(*row)
