input_str = input()
bomb = input()

stack = []
for i in input_str:
    stack.append(i)
    if i == bomb[-1] and stack[-len(bomb):] == list(bomb):
        for j in range(len(bomb)):
            stack.pop()

if stack:
    for ans in stack:
        print(ans,end='')
else:
    print('FRULA')