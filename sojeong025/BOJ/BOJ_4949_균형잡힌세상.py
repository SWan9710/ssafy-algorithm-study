import sys
sys.stdin = open('input.txt')

# word = input()
# stack = []

while True:
    word = input()
    stack = []
    # 종료조건
    if word == '.':
        break
    for i in word:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

