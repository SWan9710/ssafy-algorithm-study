import sys
text = sys.stdin.readline().strip()
bomb = list(sys.stdin.readline().strip())

stack = []

for char in text:
    stack.append(char)
    if stack[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

print("".join(stack) if stack else "FRULA")
