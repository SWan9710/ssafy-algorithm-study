# 8방향 델타탐색
dx = [0,0,1,-1,1,-1,-1,1]
dy = [1,-1,0,0,1,-1,1,-1]

def BFS(x, y):
    visited = [[0] * M for _ in range(N)]
    queue = [(x, y)]
    visited[x][y] = 1
    num = 0
    while queue:
        sx, sy = queue.pop(0)
        for k in range(8):
            nx, ny = sx + dx[k], sy + dx[y]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]==0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[sx][sy] + 1

    return visited

N, M = map(int, (input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

#상어가 있는 위치 저장
shark = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            shark.append((i, j))
print(shark)

# 튜플로 저장된 위치를 하나씩 가져와서 sx, sy에 할당
for sx, sy in shark:
    print(BFS(sx, sy))