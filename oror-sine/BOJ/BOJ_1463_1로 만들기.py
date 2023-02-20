import sys
N = int(sys.stdin.readline())
dic = {1: 0, 2:1, 3:1}

def dp(X):
    if X in dic:
        return dic[X]
    dic[X] = min(dp(X // 3) + X % 3, dp(X // 2) + X % 2) + 1
    return dic[X]

print(dp(N))