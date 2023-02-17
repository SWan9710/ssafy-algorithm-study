N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for i in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False] * (N+1)
ans = 0

def dfs(v,num):
    global ans

    num += 1
    visited[v] = True

    if v == B:
        ans = num

    else:
        for i in graph[v]:
            if not visited[i]:
                dfs(i,num)

dfs(A,0)

if ans:
    print(ans-1)
else:
    print(-1)