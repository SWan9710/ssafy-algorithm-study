import sys
sys.stdin = open('단지.txt')
sys.setrecursionlimit(10**6)

def DFS(x, y):
    global cnt_num
    cnt_num += 1
    arr[x][y] = '0'

    for k in range(4):
        nx, ny = x + dx[k], y+ dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == '1':
                DFS(nx, ny)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N = int(input())
arr = [list(input()) for _ in range(N)]

count = 0
result = []

for x in range(N):
    for y in range(N):
        cnt_num = 0
        if arr[x][y] == '1':
            count += 1
            DFS(x, y)
        if cnt_num > 0:
            result.append(cnt_num)

result.sort()
print(count)
for i in result:
    print(i)