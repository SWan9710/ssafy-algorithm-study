import sys

while True:
    TTT = sys.stdin.readline().rstrip()
    if TTT == "end":
        break
    R = [[0, 0], [0, 0], [0, 0]]
    C = [[0, 0], [0, 0], [0, 0]]
    D = [[0, 0], [0, 0]]
    X = O = B = 0
    condition = [0, 0]
    for i, char in enumerate(TTT):
        r = i//3
        c = i % 3
        if char != ".":
            j = 1 if char == "O" else 0
            if j:
                O += 1
            else:
                X += 1
            R[r][j] += 1
            if R[r][j] == 3:
                condition[j] += 1

            C[c][j] += 1
            if C[c][j] == 3:
                condition[j] += 1

            if r == c:
                D[0][j] += 1
                if D[0][j] == 3:
                    condition[j] += 1

            if r == 2-c:
                D[1][j] += 1
                if D[1][j] == 3:
                    condition[j] += 1
        else:
            B += 1

    if (not condition[0] and not condition[1] and not B and X-1 <= O < X) or \
            (not condition[0] and condition[1] and X == O) or \
            (condition[0] and not condition[1] and X - 1 == O):
        print("valid")
    else:
        print("invalid")
