import sys
n = int(sys.stdin.readline())
target = tuple(int(sys.stdin.readline()) for _ in range(n))

stack = []
ans = ""
idx = 0

for i in range(1, n+1):
    stack.append(i)
    ans += "+"
    while stack and idx < n and stack[-1] == target[idx]:
        stack.pop()
        ans += "-"
        idx += 1

if idx == n:
    print(*ans, sep="\n")
else:
    print("NO")
