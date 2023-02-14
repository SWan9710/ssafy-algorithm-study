arr = [list(map(int, input().split())) for _ in range(9)]

max = arr[0][0]
for i in range(9):
    for j in range(9):
        if arr[i][j] >= max:
            max = arr[i][j]
            index = [i+1, j+1]

print(max)
print(*index)
