import sys
sys.stdin = open('input.txt')

target = input()
pattern = input()

stack = []

for char in target:
    stack.append(char)

    if stack[-1] == pattern[-1] and ''.join(stack[-len(pattern):]) == pattern and len(stack) >= len(pattern):
        for _ in range(len(pattern)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')

