import sys
N = int(sys.stdin.readline())
i = 1
num = 666
while i < N:
    num += 1
    if "666" in str(num):
        i+= 1
print(num)
