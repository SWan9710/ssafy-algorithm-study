# import sys
# sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x,y):
    global count
    apart[x][y] = '0'
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and apart[nx][ny] == '1':
            DFS(nx,ny)
            

N = int(input())
apart = [list(input()) for _ in range(N)]
danji = []

for j in range(N):
    for k in range(N):
        if apart[j][k] == '1':
            count = 0
            DFS(j,k)
            danji.append(count)

print(len(danji))
danji.sort()
for i in danji:
    print(i)




