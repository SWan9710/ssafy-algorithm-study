N,M = map(int,input().split())
basket = [i for i in range(N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    basket = basket[:i] + list(reversed(basket[i:j+1])) + basket[j+1:]

print(*basket[1:])