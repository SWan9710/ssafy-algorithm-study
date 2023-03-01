import sys
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
adjacency_list = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
mini = -1
for _ in range(m):
    parent, child = map(int, sys.stdin.readline().split())
    adjacency_list[parent].append(child)
    adjacency_list[child].append(parent)


def dfs(current, target, cnt):
    global visited
    global mini
    if current == target:
        if mini == -1 or mini > cnt:
            mini = cnt

    visited[current] = True

    for node in adjacency_list[current]:
        if not visited[node]:
            dfs(node, target, cnt+1)

dfs(a, b, 0)
print(mini)
