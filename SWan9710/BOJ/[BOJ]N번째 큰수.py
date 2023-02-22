from heapq import heappush, heappop
heap = []

N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))

    for j in arr:
        heappush(heap, j)
        if len(heap) > N:
            heappop(heap)
print(heap[0])
