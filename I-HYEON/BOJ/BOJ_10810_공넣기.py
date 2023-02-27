N,M = map(int,input().split())

basket = [0 for _ in range(N+1)]

for _ in range(M):
    i,j,k = map(int,input().split())
    for b in range(i,j+1):
        basket[b] = k

ans = basket[1:]
print(*ans)