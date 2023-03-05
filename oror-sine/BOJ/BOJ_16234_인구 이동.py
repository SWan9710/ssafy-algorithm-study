import sys
N, L, R = map(int, sys.stdin.readline().split())
grid = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]

def bfs(coord):
    stack = [coord]
    visited[coord[0]][coord[1]] = True
    nations = [coord]
    populations = grid[coord[0]][coord[1]]
    nation_cnt = 1
    while stack:
        r, c = stack.pop()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= (nr := r+dr) < N and 0 <= (nc := c+dc) < N:
                if visited[nr][nc]:
                    continue
                if L <= abs(grid[r][c] - grid[nr][nc]) <= R:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
                    nations.append((nr, nc))
                    populations += grid[nr][nc]
                    nation_cnt  += 1
    if nation_cnt == 1:
        return False
    average = populations//nation_cnt
    for nation in nations:
        grid[nation[0]][nation[1]] = average
    return True

loop = True
days = -1
while loop:
    days += 1
    visited = [[False]*N for _ in range(N)]
    loop = False
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            if bfs((r,c)):
                loop = True
print(days)
