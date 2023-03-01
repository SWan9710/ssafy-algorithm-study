import sys
fibos = [0, 1]
n = int(sys.stdin.readline())
i = 2
while i <= n:
    fibos.append(fibos[i-1] + fibos[i-2])
    i += 1
print(fibos[n])
