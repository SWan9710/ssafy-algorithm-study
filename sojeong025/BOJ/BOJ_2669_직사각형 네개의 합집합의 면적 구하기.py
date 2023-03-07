'''
구현 방법 아이디어
1. 101 * 101 matrix 생성
2. x1, x2, y1, y2 좌표로 구성된 사각형 부분만 1로 바꿔줌
3. 그 부분을 count해서 결과값 추출
'''

import sys
sys.stdin = open('input.txt')

mat = [[0] * 101 for _ in range(101)]

# 4개의 직사각형
count = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            if mat[i][j] == 0:
                mat[i][j] += 1
                count += 1
print(count)





