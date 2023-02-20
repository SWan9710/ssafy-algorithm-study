import sys, heapq
N = int(sys.stdin.readline())
lst = [int(i) for i in sys.stdin.readline().split()]
for _ in range(N-1):
    row = [int(i) for i in sys.stdin.readline().split()]
    for cell in row:
        heapq.heappushpop(lst, cell)
print(lst[0])
