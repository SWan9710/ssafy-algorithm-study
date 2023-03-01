'''
구현방법 아이디어 
델타 - snail이랑 비슷한느낌..?
'''


C, R = map(int, input().split())
K = int(input())
mat = [[0] * R for _ in range(C)]


# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

count = 1
x, y = 0, 0
dir = 0
mat[x][y] = count

if K > C*R:
    print(0)
    exit()

while count < C*R:
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < C and 0 <= ny < R and mat[nx][ny] == 0: 
        count += 1
        mat[nx][ny] = count
        x, y = nx, ny
    else:
        dir += 1
        if dir >= 4:
            dir = 0

for i in range(C):
    for j in range(R):
        if mat[i][j] == K:
            print(i+1, j+1)


                

