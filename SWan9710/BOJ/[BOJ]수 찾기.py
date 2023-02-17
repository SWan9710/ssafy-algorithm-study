import sys
sys.stdin = open('input.txt')

def search(arr, N):
    start = 0
    end = len(arr) -1

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] > N:
            end = middle -1

        elif arr[middle] < N:
            start = middle +1

        else:
            return 1
    return 0




N = int(input())
arr1 = list(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for N in arr2:
    print(search(arr1, N))