import sys
sys.setrecursionlimit(10**6)    # 재귀호출 오류 줄여주는 코드

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def DFS(sx, sy):
    arr[sx][sy] = 0
    # 델타탐색
    for k in range(4):
        nx = sx + dx[k]
        ny = sy + dy[k]

        if 0 <= nx < M and 0 <= ny < N:
            # 배추가 심어져 있을때
            if arr[nx][ny] == 1:
                DFS(nx,ny)
  
T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())

    arr = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    start_num = []

    # 배추밭 만들기
    for i in range(K):
        x, y = map(int, input().split())
        start_num.append((x,y))
        arr[x][y] = 1

    # 시작지점 뽑기
    count = 0
    for sx in range(M):
        for sy in range(N):
            if arr[sx][sy] == 1:
                count += 1
                DFS(sx, sy)
    print(count)
