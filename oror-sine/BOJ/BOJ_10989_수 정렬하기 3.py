import sys
cnts = {}

for _ in range(int(sys.stdin.readline())):
    key = int(sys.stdin.readline())
    if cnts.get(key):
        cnts[key] += 1
    else:
        cnts[key] = 1

for key in sorted(cnts):
    for _ in range(cnts[key]):
        print(key)
