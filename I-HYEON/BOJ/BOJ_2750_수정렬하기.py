#버블소트 사용해서 정렬하기

N = int(input())

L = []
for i in range(N):
    L.append(int(input()))

for i in range(N-1,-1,-1):
    for j in range(i):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]

for i in range(N):
    print(L[i])