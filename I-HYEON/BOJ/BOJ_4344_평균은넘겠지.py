C = int(input())
for i in range(C):
    line = list(map(int,input().split()))
    N = line[0]
    line.remove(N)
    average = sum(line) / N
    cnt = 0
    for j in line:
        if j > average:
            cnt += 1
    print(str('%.3f' % round(cnt/N * 100, 3))+'%')
