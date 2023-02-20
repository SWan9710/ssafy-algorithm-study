import sys
N, M = map(int, sys.stdin.readline().split())
lst = [int(i) for i in range(1,N+1)]
visited = 0
ans = []


def dfs(sequence):
    global visited
    global ans
    if len(sequence) == M:
        ans.append(sequence)
        return

    for j in range(N):
        if visited & (1 << j):
            continue
        else:
            visited += 1 << j
            sequence.append(lst[j])
            dfs(sequence.copy())
            visited -= 1 << j
            sequence.pop()


dfs([])
for sequence in ans:
    print(*sequence)
