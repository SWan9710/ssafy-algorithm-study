# 1. 가로, 세로 주어짐

def div(arr, N):
    result = 0
    for i in range(len(arr)-1):
        div = arr[i+1] - arr[i]
        if div > result:
            result = div
    return result

row, col = map(int, input().split())
row_lst = [0]
col_lst = [0]
row_lst.append(col)
col_lst.append(row)

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    if x == 0:
        row_lst.append(y)
    else:
        col_lst.append(y)

row_lst.sort()
col_lst.sort()

row_result = div(row_lst, row)
col_result = div(col_lst, col)
print(row_result * col_result)
