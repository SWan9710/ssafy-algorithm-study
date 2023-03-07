N = int(input())    # 0 ~ 30000
i = 0
total_result = []
while i != N:
    result = []
    result.append(N)
    result.append(N - i)

    j = 0
    while True:
        if result[j] - result[j+1] >= 0:
            result.append(result[j]-result[j+1])
            j += 1
        else:
            break
    if len(total_result) < len(result):
        total_result = result
    i += 1
print(len(total_result))
print(*total_result)