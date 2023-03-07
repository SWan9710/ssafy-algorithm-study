N,M = map(int,input().split())

arr =[]
def dfs():
    if len(arr) == M:
        print(*arr)
    for i in range(1,N+1):
        if not i in arr:
            arr.append(i)
            dfs()
            arr.remove(i)

dfs()