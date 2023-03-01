arr = [[0] * 100 for _ in range(100)]
result = 0
T = int(input())
for _ in range(1, T+1):
    x, y = list(map(int, input().split()))

    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1


for color in arr:
    result += color.count(1)
print(result)
