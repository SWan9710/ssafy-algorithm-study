import sys
K, N = map(int, sys.stdin.readline().split())
cables = tuple(int(sys.stdin.readline()) for _ in range(K))
maxi = max(cables)

def binary_search(lst):
    left, right = 0, len(lst)-1
    while left <= right:
        mid = (left + right) // 2
        parts1 = sum(cable//lst[mid] for cable in cables)
        parts2 = sum(cable//(lst[mid]+1) for cable in cables)
        if parts1 >= N and parts2 <= N-1:
            return lst[mid]
        elif parts2 > N-1:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    
print(binary_search(range(1, maxi+1)))
