import sys
input = sys.stdin.readline

while True:

    mystr = input().rstrip()  # 문자열을 받아온다.

    if mystr == '.':
        break

    ans = 'yes'
    stack = []
    for i in mystr:  # 문자열을 순회하면서 검사한다.
        if not i in '()[]':
            continue
        elif i in '([':
            stack.append(i)
        elif i == ')':
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
        ans = 'no'

    print(ans)