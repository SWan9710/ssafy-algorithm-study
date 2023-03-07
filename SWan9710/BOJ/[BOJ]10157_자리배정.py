import sys
sys.stdin = open('input.txt')

def search(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == find_num:
                return i+1, j+1
    return 0

N, M = map(int, input().split())
find_num = int(input())
arr = [[0] * N for _ in range(M)]

num = 1
col = 1
row = 0

while True:
    # 시작한줄 채우기(세로로 밑에서 위로 올라가기)
    for i in range(M-1,-1,-1):
        if arr[i][row] != 0:
            continue
        arr[i][row] = num
        num += 1

    # 위에서 가로로 한줄 채우기
    for i in range(N):
        if arr[row][i] != 0:
            continue
        arr[row][i] = num
        num += 1

    # 끝에서 세로로 아래로 가면서 채우기
    for i in range(M):
        if arr[i][N-col] != 0:
            continue
        arr[i][N-col] = num
        num += 1

    # 바닥 오른쪽에서 왼쪽으로 채우기
    for i in range(N-1,-1,-1):
        if arr[M-col][i] != 0:
            continue
        arr[M-col][i] = num
        num += 1

    row += 1
    col += 1

    if num == N*M+1:
        break

# 정답을 출력하기 위해 배열을 90도 회전시키기
arr2 = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        arr2[i][j] = arr[M-j-1][i]

for i in arr2:
    print(i)

result = search(arr2)
if type(result) == tuple:
    print(*result)
else:
    print(result)