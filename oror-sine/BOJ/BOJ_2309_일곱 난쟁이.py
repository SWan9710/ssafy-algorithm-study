import sys
dwarves = sorted([int(sys.stdin.readline()) for _ in range(9)])
sum_ = sum(dwarves)-100
for i in dwarves:
    if len(dwarves)==7:
        break
    for j in dwarves:
        if i != j and i+j == sum_:
            dwarves.remove(i)
            dwarves.remove(j)      
            break
for i in dwarves:
    print(i)
