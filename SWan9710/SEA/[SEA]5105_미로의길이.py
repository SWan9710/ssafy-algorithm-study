import sys
sys.stdin = open('input.txt')

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(x, y):

    queue = [(x, y)]
    visited[x][y] = 1

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

                if arr[nx][ny] == 3:
                    return visited[x][y] - 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j

    print(f'#{tc}',BFS(x,y))