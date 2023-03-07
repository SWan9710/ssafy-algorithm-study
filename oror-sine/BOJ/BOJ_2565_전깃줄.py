import sys
N = int(sys.stdin.readline())
wires = sorted([[int(i) for i in input().split()] for _ in range(N)])
dp = [1]*N
for i in range(N):
    if nonoverlapping := [j for j in range(i) if wires[i][1] > wires[j][1]]:
        dp[i] = dp[max(nonoverlapping, key=lambda x: dp[x])] + 1
print(N-max(dp))
