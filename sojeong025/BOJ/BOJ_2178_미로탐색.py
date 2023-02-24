import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def search(x, y, cnt):
    queue = [(x, y, cnt)]
    while queue:
        x, y, cnt = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = cnt + 1
                if nx == N-1 and ny == M-1:
                    return visited[nx][ny]
                queue.append((nx, ny, cnt+1))


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(search(0, 0, 1))
