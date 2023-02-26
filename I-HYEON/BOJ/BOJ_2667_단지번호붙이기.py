import sys
input = sys.stdin.readline


def bfs(x,y):
    global home_cnt
    home_cnt = 1
    town[x][y] = 0
    Q = [(x,y)]

    while Q:
        now = Q.pop(0)
        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and town[ni][nj] == 1:
                town[ni][nj] = 0
                home_cnt += 1
                Q.append((ni,nj))

    return home_cnt


N = int(input().rstrip())
town = []
for i in range(N):
    town.append(list(map(int,list(input().rstrip()))))

complex_cnt = 0
home_cnts = []
di = [-1,0,1,0]
dj = [0,1,0,-1]
for i in range(N):
    for j in range(N):

        if town[i][j] == 1:
            complex_cnt += 1
            home_cnts.append(bfs(i,j))

home_cnts.sort()
print(complex_cnt)
for ans in home_cnts:
    print(ans)