room = int(input())

tc = room - 1
n = 1

while tc > 0:
    tc -= 6*n
    n += 1

print(n)