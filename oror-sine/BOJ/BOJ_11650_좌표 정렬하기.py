import sys
input = sys.stdin.readline

T = int(input())
lst = []
for _ in range(T):
    lst.append(tuple(int(i) for i in input().split()))
for x,y in sorted(lst):
    print(x, y)
