import sys
grid = [[False for _ in range(100)] for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(lambda x: int(x)-1, sys.stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[y][x] = True
area = 0
for row in grid:
    for cell in row:
        if cell:
            area += 1
print(area)
