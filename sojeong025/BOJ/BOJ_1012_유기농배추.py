import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x, y):
    global count
    stack = [(x, y)]
    arr[x][y] = 0   # 방문 표시

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 1:
                stack.append((nx, ny))
                arr[nx][ny] = 0
    count += 1


T = int(input())
for tc in range(1, T+1):
    # M: 배추밭 가로길이 N: 배추밭 세로길이
    M, N, K = map(int, input().split())
    count = 0
    # 배추밭
    arr = [[0]*N for _ in range(M)]

    for i in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1

    for j in range(M):
        for k in range(N):
            if arr[j][k] == 1:
                DFS(j, k)

    print(count)

