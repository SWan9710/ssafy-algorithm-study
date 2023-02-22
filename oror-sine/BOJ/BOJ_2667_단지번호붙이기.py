import sys
N = int(sys.stdin.readline())
grid = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(N)]
house_cnts = []
for r in range(N):
    for c in range(N):
        if grid[r][c]:
            grid[r][c] = 0
            house_cnt = 1
            stack = [(r, c)]
            while stack:
                y, x = stack.pop()
                for dy, dx in (-1, 0), (0, -1), (0, 1), (1, 0):
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < N and 0 <= nx < N and grid[ny][nx]:
                        grid[ny][nx] = 0
                        house_cnt += 1
                        stack.append((ny, nx))
            house_cnts.append(house_cnt)
print(len(house_cnts))
for cnt in sorted(house_cnts):
    print(cnt)
