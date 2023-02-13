N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

# for i in range(N-1,-1,-1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
arr.sort()

for i in range(N):
    print(arr[i])