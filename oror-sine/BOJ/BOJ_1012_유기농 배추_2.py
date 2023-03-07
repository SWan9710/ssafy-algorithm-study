import sys

T = int(sys.stdin.readline())

ds = tuple(zip((0, -1, 1, 0), 
               (-1, 0, 0, 1)))

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
                    if cabbages.get((y+dy, x+dx)):
                        cabbages[(y+dy, x+dx)] = 0
                        stack.append((y+dy, x+dx))
            cnt += 1
    print(cnt)
