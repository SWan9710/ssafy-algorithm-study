import sys
sys.stdin = open('input.txt')

while True:
    stack = []
    arr = input()
    if arr == '.':
        break
    for i in arr:
        if i =='(' or i == '[':
            stack.append(i)

        else:
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
                    break
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(i)
                    break
    if stack:
        print('no')
    else:
        print('yes')
