import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatoes = [[] for _ in range(N)]
queue = deque([])
for r in range(N):
    for c, cell in enumerate(sys.stdin.readline().split()):
        tomatoes[r].append(int(cell))
        if tomatoes[r][c] == 1:
            queue.append((r, c))

ds = tuple(zip((0, -1, 1, 0),
              (-1, 0, 0, 1)))

def ripen():
    cnt = -1
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for d in ds:
                nr, nc = r+d[0], c+d[1]
                if 0 <= nr < N and 0 <= nc < M and tomatoes[nr][nc] == 0:
                    queue.append((nr, nc))
                    tomatoes[nr][nc] = 1
        cnt += 1
    for row in tomatoes:
        for cell in row:
            if cell == 0:
                return -1
    return cnt


print(ripen())
