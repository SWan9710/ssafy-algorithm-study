def calc():
    global visited
    power_1 = 0
    power_2 = 0
    for i in range(N):
        for j in range(i+1, N):
            if visited & ((1 << i)+(1 << j)) == (1 << i)+(1 << j):
                power_1 += S[i][j] + S[j][i]
            elif ((1 << N) - visited - 1) & ((1 << i)+(1 << j)) == (1 << i)+(1 << j):
                power_2 += S[i][j] + S[j][i]
    return abs(power_1-power_2)

def dfs(n, idx):
    global visited
    if n == N // 2:
        power_d_lst.append(calc())
        return
    for i in range(idx, N):
        if not(visited & (1 << i)):
            visited += 1 << i
            dfs(n+1, i+1)
            visited -= 1 << i

N = int(input())
S = [[int(i) for i in input().split()] for _ in range(N)]
visited = 1
power_d_lst = []
dfs(1, 0)
print(min(power_d_lst))