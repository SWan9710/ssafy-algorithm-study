import sys
from collections import deque

ds = tuple(zip((-1, 1, 0, 0, 0, 0),
         (0, 0, -1, 1, 0, 0),
         (0, 0, 0, 0, -1, 1)))

queue = deque([])

M, N, H = map(int, sys.stdin.readline().split())
tomatoboxes = []
for h in range(H):
    tomatobox = []
    for r in range(N):
        tomatobox.append([int(tomato) for tomato in sys.stdin.readline().split()])
        for c, tomato in enumerate(tomatobox[r]):
            if tomato == 1:
                queue.append((h,r,c))
    tomatoboxes.append(tomatobox)
def ripen():
    cnt = -1
    while queue:
        for _ in range(len(queue)):
            h, r, c = queue.popleft()
            for dh, dr, dc in ds:
                nh, nr, nc = h+dh, r+dr, c+dc
                if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and tomatoboxes[nh][nr][nc] == 0:
                    queue.append((nh, nr, nc))
                    tomatoboxes[nh][nr][nc] = 1
        cnt += 1
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if not tomatoboxes[h][r][c]:
                    return -1
    return cnt

print(ripen())
