import sys
C, R = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
cuts = [[0], [0]]
for _ in range(N):
    axis, n = map(int, sys.stdin.readline().split())
    cuts[axis].append(n)
cuts[0].append(R)
cuts[1].append(C)
cuts[0].sort()
cuts[1].sort()
maxi = 0
for c in range(len(cuts[0])-1):
    for r in range(len(cuts[1])-1):
        area = (cuts[0][c + 1] - cuts[0][c]) * (cuts[1][r + 1] - cuts[1][r])
        if maxi < area:
            maxi = area
print(maxi)
