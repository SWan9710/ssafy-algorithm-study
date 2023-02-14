import sys
N = int(sys.stdin.readline())
trees = sorted(list(map(int, sys.stdin.readline().split())))
days = remaining = 0

while trees:
    days += 1
    tree = trees.pop() + 1
    if remaining < tree:
        remaining = tree
    remaining -= 1

print(days + remaining +1)
