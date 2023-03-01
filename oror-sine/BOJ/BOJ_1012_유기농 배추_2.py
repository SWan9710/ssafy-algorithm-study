import sys

T = int(sys.stdin.readline())

ds = zip((0, -1, 1, 0), 
         (-1, 0, 0, 1))

for _ in range(T):
    _, _, K = map(int, sys.stdin.readline().split())
    cabbages = {tuple(int(i) for i in sys.stdin.readline().split()): 1 for _ in range(K)}
    cnt = 0
    for coord in cabbages.keys():
        if cabbages[coord]:
            cabbages[coord] = 0
            stack = [coord]
            while stack:
                y, x= stack.pop()
                for dy, dx in ds:
                    ny, nx = y+dy, x+dx
                    if (ny, nx) in cabbages:
                        cabbages[(ny, nx)] = 0
                        stack.append((ny, nx))
            cnt += 1
    print(cnt)
