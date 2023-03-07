import sys
canvas = [[0]*100 for _ in range(100)]
N = int(sys.stdin.readline())
min_x = min_y = 100
max_x = max_y = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x+10)
    max_y = max(max_y, y+10)
    for r in range(y, y+10):
        canvas[r][x:x+10] = [1]*10

ans = 0           
for row in canvas[min_y:max_y]:
    ans += sum(row[min_x:max_x])

print(ans)
