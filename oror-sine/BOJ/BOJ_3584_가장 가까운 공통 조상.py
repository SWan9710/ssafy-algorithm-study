import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    parents = {}
    for i in range(N-1):
        parent, child = map(int, sys.stdin.readline().split())
        parents[child] = parent
    A, B = map(int, sys.stdin.readline().split())
    ancestors = []
    for _ in range(N):
        if A in ancestors:
            print(A)
            break
        if A:
            ancestors.append(A) 
            A = parents.get(A)
        if B in ancestors:
            print(B)
            break
        if B:
            ancestors.append(B)
            B = parents.get(B)
