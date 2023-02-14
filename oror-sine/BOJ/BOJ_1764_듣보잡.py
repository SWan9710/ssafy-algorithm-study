import sys
input = sys.stdin.readline

N, M = map(int, input().split())
never_heard = {input().strip() for _ in range(N)}
never_seen = {input().strip() for _ in range(M)}
intersection = sorted(list(never_heard & never_seen))

print(len(intersection))
for name in intersection:
    print(name)