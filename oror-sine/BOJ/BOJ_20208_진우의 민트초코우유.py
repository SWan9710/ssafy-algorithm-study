import sys
HOME, MINT = "1", "2"
N, M, H = map(int, sys.stdin.readline().split())
mints = [tuple()]
for r in range(N):
    for c, cell in enumerate(sys.stdin.readline().split()):
        if cell == MINT:
            mints.append((r, c))
        elif cell == HOME:
            mints[0] = (r, c)

vanished = [False]*len(mints)
distances = [[0]*len(mints) for _ in range(len(mints))]
for i in range(len(mints)):
    for j in range(i+1, len(mints)):
        distances[i][j] = distances[j][i] = abs(mints[i][0]-mints[j][0]) + abs(mints[i][1]-mints[j][1])


def backtrack(i, hp, cnt):
    maxi = 0 if distances[i][0] > hp else cnt

    for j in range(1, len(mints)):
        if vanished[j]:
            continue
        if distances[i][j] > hp:
            continue

        vanished[j] = True
        maxi = max(maxi, backtrack(j, hp - distances[i][j] + H, cnt + 1))
        vanished[j] = False

    return maxi


print(backtrack(0, M, 0))
