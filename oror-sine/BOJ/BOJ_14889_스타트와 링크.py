import sys

N = int(sys.stdin.readline())
abilities = [sys.stdin.readline().split() for _ in range(N)]
mini = None

for selected in range((1 << (N >> 1))-1, 1 << (N-1)):
    if bin(selected).count("1") == N >> 1:
        diff = 0
        for i in range(N):
            for j in range(i + 1, N):
                if i == j:
                    continue
                if selected & ((1 << i) + (1 << j)) == (1 << i) + (1 << j):
                    diff += int(abilities[i][j]) + int(abilities[j][i])
                elif ((1 << N) - 1 - selected) & ((1 << i) + (1 << j)) == (1 << i) + (1 << j):
                    diff -= int(abilities[i][j]) + int(abilities[j][i])
        diff = abs(diff)
        if mini is None or mini > diff:
            mini = diff
    if mini == 0:
        break
print(mini)
