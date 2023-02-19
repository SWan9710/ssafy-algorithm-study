import sys


def postfix(infix):
    operators = []
    tokens = []
    for token in infix:
        if token == "(":
            operators.append(token)
        elif token == ")":
            while operators[-1] != "(":
                tokens.append(operators.pop())
            operators.pop()
        elif token in "+-*/":
            while operators[-1] != "(" and not(operators[-1] in "+-" and token in "*/"):
                tokens.append(operators.pop())
            operators.append(token)
        else:
            tokens.append(token)
    return "".join(tokens)


expression = "("+sys.stdin.readline().rstrip()+")"
print(postfix(expression))
