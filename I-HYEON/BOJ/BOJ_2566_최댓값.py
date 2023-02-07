import sys
input = sys.stdin.readline

matrix = []
for i in range(9):
    matrix.append(list(map(int,input().split())))

keymax = 0
k = 0
j = 0
for i in range(9):
    for j in range(9):
        if keymax <= matrix[i][j]: #여기서 '='이 빠지면 런타임에러가 뜨는데 왜인지 모르겠음
            keymax = matrix[i][j]
            k = i+1
            l = j+1

print(keymax)
print(k,l)