import sys
while True:
    text = sys.stdin.readline().rstrip()
    if text == ".":
        break
    
    stack = []
    for char in text:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack:
                print("no")
                break

            if stack[-1] == "(" and char == ")":
                stack.pop()
            elif stack[-1] == "[" and char == "]":
                stack.pop()
            else:
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")
