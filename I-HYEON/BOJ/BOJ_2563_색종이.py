matrix = [[0 for i in range(100)] for i in range(100)]

N = int(input())

for n in range(N):
    a,b = map(int, input().split())
    
    for i in range(10):
        for j in range(10):
            if matrix[a+i][b+j] == 0:
                matrix[a+i][b+j] = 1
            else:
                pass

cnt = 0
for i in range(100):
    cnt += sum(matrix[i])

print(cnt)