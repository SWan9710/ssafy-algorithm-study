import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())

    arr =[]
    for i in range(100):
        input_arr = list(map(int, input().split()))
        arr.append(input_arr)

    # 가로의 합
    row = 0
    for i in range(100):
        row_result = 0
        for j in range(100):
            row_result += arr[i][j]
            if row_result > row:
                row = row_result
    # print('가로',row)

    #세로의 합
    col = 0
    for i in range(100):
        col_value = 0
        for j in range(100):
            col_value += arr[j][i]
        if col_value > col:
            col = col_value
    # print('세로',col)

    # 대각선 왼쪽위에서 오른쪽 아래로
    left_top = 0
    for i in range(100):
        left_top += arr[i][i]
    # print('왼쪽위',left_top)

    # 대각선 오른쪽위에서 왼쪽 아래로
    right_top = 0
    for i in range(100):
        right_top += arr[i][99-i]
    # print('오른쪽위',right_top)

    result = [row,col,left_top,right_top]
    total_result = 0
    for i in range(4):
        if total_result < result[i]:
            total_result = result[i]
    print(f'#{N} {total_result}')
