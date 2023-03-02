import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 가로세로
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    # 대각선
    sx = [-1,-1,1,1]
    sy = [-1,1,1,-1]
    result_d = 0
    result_s = 0
    for i in range(N):
        for j in range(N):
            count_d = 0
            count_d += arr[i][j]
            # 가로세로 방향에 대한 탐색
            for k1 in range(4):
                for d1 in range(1,M):
                    nx1 = i + dx[k1] * d1
                    ny1 = j + dy[k1] * d1

                    if 0 <= nx1 < N and 0 <= ny1 < N:
                        count_d += arr[nx1][ny1]

            if result_d < count_d:
                result_d = count_d

            # 대각선 방향에 대한 탐색
            count_s = 0
            count_s += arr[i][j]
            for k2 in range(4):
                for d2 in range(1,M):
                    nx2 = i + sx[k2] * d2
                    ny2 = j + sy[k2] * d2
                    if 0 <= nx2 < N and 0 <= ny2 < N:
                        count_s += arr[nx2][ny2]
            if result_s < count_s:
                result_s = count_s
    if result_d > result_s:
        print(f'#{tc}',result_d)
    else:
        print(f'#{tc}', result_s)
