import sys
w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
p += t
q += t
p = w - p % w if (p//w) % 2 else p % w
q = h - q % h if (q//h) % 2 else q % h
print(p, q)
