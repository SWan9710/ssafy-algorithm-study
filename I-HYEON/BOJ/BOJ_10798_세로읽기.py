# 이차원배열을 받아와서 세로로 읽는데 인덱스 에러가 나면 PASS하는 식으로 하면 될듯?

arr = [list(input()) for _ in range(5)]

for j in range(15):
    for i in range(5):
        try:
            print(arr[i][j],end='')
        except IndexError:
            pass