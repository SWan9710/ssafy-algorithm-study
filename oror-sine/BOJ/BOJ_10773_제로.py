import sys
T = int(sys.stdin.readline())
num_stack = []
for _ in range(T):
    num = int(sys.stdin.readline())
    if num:
        num_stack.append(num)
    else:
        num_stack.pop()
print(sum(num_stack))
