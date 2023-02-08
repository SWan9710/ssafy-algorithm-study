# def siftdown(heap, root, child):
#     item = heap[child]
#     while child > root:
#         parent = (child-1)>>1
#         parent_item = heap[parent]
#         if item < parent_item:
#             heap[child] = parent_item
#             child = parent
#             continue
#         break
#     heap[child] = item

# def siftup(heap, parent):
#     leaf = len(heap)
#     root = parent
#     item = heap[parent]
#     child = (parent<<1) + 1
#     while child < leaf:
#         right = child + 1
#         if right < leaf and heap[right] < heap[child]:
#             child = right
#         heap[parent] = heap[child]
#         parent = child
#         child = (parent<<1) + 1
#     heap[parent] = item
#     siftdown(heap, root, parent)

# def heapify(iterable):
#     n = len(iterable)
#     for i in reversed(range(n//2)):
#         siftup(iterable, i)

# def heappop(heap):
#     item = heap.pop()
#     if heap:
#         heap[0], item = item, heap[0]
#         siftup(heap, 0)
#     return item

# def heappush(heap, item):
#     n = len(heap)
#     heap.append(item)
#     siftdown(heap, 0, n-1)

# def heappushpop(heap, item):
#     if heap and heap[0] < item:
#         heap[0], item = item, heap[0]
#         siftup(heap, 0)
#     return item

# def heapreplace(heap, item):
#     heap[0], item = item, heap[0]
#     siftup(heap, 0)
#     return item


# If available, use C implementation  <- 도저히 따라 잡을 수 없었던 이유...
from heapq import * 

def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        if len(scoville) == 1: return -1
        heappush(scoville, heappop(scoville) + (heappop(scoville)<<1))
        cnt += 1
    return cnt
