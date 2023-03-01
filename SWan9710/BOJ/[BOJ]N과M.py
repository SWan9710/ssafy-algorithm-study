N, M  = map(int, input().split())

lst = list(range(1, N+1))
visited = [1] * N

a = ''
def f(i, k, res):
    global visited, a
    if i == k:
        print(*res)
        return
    for j in range(N):
        if visited[j]:
            visited[j] = 0
            f(i + 1, k, res+[lst[j]])
            visited[j] = 1

f(0, M, [])