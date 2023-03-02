import sys
N, K = map(int, sys.stdin.readline().split())
M = [0]*6
F = [0]*6
for _ in range(N):
    sex, grade = map(int, sys.stdin.readline().split())
    if sex: M[grade-1] += 1
    else:   F[grade-1] += 1

ans = 0
for grade in range(6):
    ans += M[grade]//K + (1 if M[grade]%K else 0)
    ans += F[grade]//K + (1 if F[grade]%K else 0)
print(ans)
