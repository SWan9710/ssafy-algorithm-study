import sys
N = int(sys.stdin.readline())
lst = [int(i) for i in sys.stdin.readline().split()]
visited = 0
results = []


def dfs(sequence):
    global visited
    global results

    if len(sequence) == N:
        result = 0
        for i in range(1, N):
            result += abs(sequence[i-1]-sequence[i])
        results.append(result)
        return

    for i in range(N):
        if not visited & (1 << i):
            visited += (1 << i)
            sequence.append(lst[i])
            dfs(sequence)
            sequence.pop()
            visited -= (1 << i)


dfs([])
print(max(results))
