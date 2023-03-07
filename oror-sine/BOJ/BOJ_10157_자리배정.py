import sys
C, R = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
seats = [[1]*(C+2)] + [([1]+[0]*C+[1]) for _ in range(R)] + [[1]*(C+2)]
y = x = 1
ds = ((1, 0), (0, 1), (-1, 0), (0, -1))
idx = 0
if K > C*R:
    print(0)
else:
    for i in range(1, C*R+1):
        if i == K:
            print(x, y)
            break
        seats[y][x] = i
        dy, dx = ds[idx]
        if seats[y+dy][x+dx]:
            idx = (idx+1)%4
            dy, dx = ds[idx]
        y += dy
        x += dx
