import sys
N = int(sys.stdin.readline())
order = []
for student, num in enumerate(map(int, sys.stdin.readline().split())):
    order.insert(num, student+1)
print(*order[::-1])
