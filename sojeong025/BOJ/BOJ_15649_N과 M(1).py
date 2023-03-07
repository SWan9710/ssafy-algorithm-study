import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
stack = []

def DFS():
    if len(stack) == M:
        print(' '.join(map(str,stack)))

    for i in range(1, N+1):
        if i not in stack:
            stack.append(i)
            DFS()
            stack.pop()

DFS()