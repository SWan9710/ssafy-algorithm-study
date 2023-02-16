formula = input()
priority = {'(':0, '+':1, '-':1, '*':2, '/':2}

result = []
stack = []

for a in formula:
    if a not in '+-*/':
        if a == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        elif a == '(':
            stack.append(a)

        else:
            result.append(a)
    else:
        while stack and priority[a] <= priority[stack[-1]]:
            result.append(stack.pop())
        stack.append(a)

while stack:
    result.append(stack.pop())

for i in range(len(result)):
    print(result[i],end='')