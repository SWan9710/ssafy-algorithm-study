import sys
N = int(sys.stdin.readline())
papers = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]
grid = [[0]*1001 for _ in range(1001)]
max_x = max_y = 0
min_x = min_y = 1001

for i, paper in enumerate(papers):
    x, y, w, h = paper

    if min_x > x:
        min_x = x
    if min_y > y:
        min_y = y
    if max_x < x+w:
        max_x = x+w
    if max_y < y+h:
        max_y = y+h

    for r in range(y, y+h):
        grid[r][x:x+w] = [i+1]*w

anss = [0]*N
for row in grid[min_y:max_y]:
    for cell in row[min_x:max_x+2]:
        if cell:
            anss[cell-1] += 1

for ans in anss:
    print(ans)
