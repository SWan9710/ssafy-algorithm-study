import sys
input = sys.stdin.readline

N = int(input())
liquids = sorted([int(i) for i in input().split()])
target = abs(liquids[0]+liquids[-1])
a = i = 0
b = j = N-1

while i<j:
    next1 = abs(liquids[i+1]+liquids[j])
    next2 = abs(liquids[i]+liquids[j-1])
    if next1 < next2:
        i += 1
    else:
        j -= 1
        next1 = next2
    if next1 < target:
        target = next1
        a = i
        b = j
   
print(a,b)