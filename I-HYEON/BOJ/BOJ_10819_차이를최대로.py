N = int(input())
arr = list(map(int,input().split()))

arr.sort()

total = 0
stack = []
visited = [0 for i in range(N)]

def dfs():
    global total

    if len(stack) == N:
        temp = 0
        for j in range(N-1):
            temp += abs(stack[j] - stack[j+1])
        if total <= temp:
            total = temp

    for i in range(N):
        if visited[i]:
            continue
        stack.append(arr[i])
        visited[i] = 1
        dfs()
        stack.pop()
        visited[i] = 0

dfs()
print(total)