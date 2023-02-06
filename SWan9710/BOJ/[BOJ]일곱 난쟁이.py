arr = [int(input()) for i in range(9)]

count = 0
over = sum(arr)-100
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if arr[i] + arr[j] == over:
            if i > j:
                arr.pop(i-1)
                arr.pop(j)
            else:
                arr.pop(i)
                arr.pop(j-1)
            count = 1
            break
    if count == 1:
        break
arr.sort()
for i in arr:
    print(i)
