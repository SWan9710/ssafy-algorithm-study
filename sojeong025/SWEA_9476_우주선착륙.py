import sys
sys.stdin = open('input.txt')

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def delta(x, y):
    lst = []
    count = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            lst.append(arr[nx][ny])
            lst = sorted(lst)
    # print(lst)
    if lst[-1] - lst[0] <= K and 0 <= arr[x][y] - lst[0] <= H:
        count += 1

    return count


T = int(input())
for tc in range(1, T+1):
    N, M, K, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(1, N-1):
        for j in range(1, M-1):

            result += delta(i, j)

    print(f'#{tc} {result}')



