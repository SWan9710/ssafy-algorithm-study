import sys
k = int(sys.stdin.readline())
n = int(sys.stdin.readline())
origins = [chr(65+i) for i in range(k)]
destinations = list(sys.stdin.readline().rstrip())
legs = [sys.stdin.readline().rstrip() for _ in range(n)]

the_leg = ["*"] * (k-1)

i = 0
while legs[i][0] != "?":
    j = 0
    while j < k-1:
        if legs[i][j] == "-":
            origins[j], origins[j+1] = origins[j+1], origins[j]
            j += 2
            continue
        j += 1 
    i += 1

i = n-1
while legs[i][0] != "?":
    j = 0
    while j < k-1:
        if legs[i][j] == "-":
            destinations[j], destinations[j+1] = destinations[j+1], destinations[j]
            j += 2
            continue
        j += 1 
    i -= 1

i = 0
while i < k-1:
    if origins[i] != destinations[i]:
        origins[i], origins[i+1] = origins[i+1], origins[i]
        if origins[i] != destinations[i] or origins[i+1] != destinations[i+1]:
            the_leg = ["x"] * (k-1)
            break
        the_leg[i] = "-"
        i += 2
        continue
    i += 1

print("".join(the_leg))
