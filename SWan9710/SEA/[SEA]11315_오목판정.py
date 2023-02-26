import sys
sys.stdin = open('오목판정.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    row_result = []
    for i in range(N):
        for j in range(N):
            x, y = i, j
            count = 0
            while 0<=x<N and 0 <= y < N and arr[x][y] == 'o':
                count += 1
                if count == 5:
                    row_result.append(count)
                    break
                y += 1

    col_result = []
    for i in range(N):
        for j in range(N):
            x, y = i, j
            count = 0
            while 0<=x<N and 0 <= y < N and arr[x][y] == 'o':
                count += 1
                if count == 5:
                    col_result.append(count)
                    break
                x += 1

    LR_result = []
    for i in range(N):
        for j in range(N):
            x, y = i, j
            count = 0
            while 0<=x<N and 0 <= y < N and arr[x][y] == 'o':
                count += 1
                if count == 5:
                    LR_result.append(count)
                    break
                x += 1
                y += 1

    RL_result = []
    for i in range(N):
        for j in range(N):
            x, y = i, j
            count = 0
            while 0<=x<N and 0 <= y < N and arr[x][y] == 'o':
                count += 1
                if count == 5:
                    RL_result.append(count)
                    break
                x += 1
                y -= 1

    if row_result or col_result or LR_result or RL_result:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

