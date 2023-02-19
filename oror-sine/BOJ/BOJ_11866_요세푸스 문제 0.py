N, K = map(int, input().split())
circle = list(map(str, range(1, N+1)))
idx = 0
josephus = []
while circle:
    idx = (idx+K-1) % len(circle)
    josephus.append(circle.pop(idx))
print("<", ", ".join(josephus), ">", sep="")
