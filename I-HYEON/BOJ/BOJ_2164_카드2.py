from collections import deque

N = int(input())

cards = deque()

for i in range(N,0,-1):
    cards.append(i)

while len(cards) > 1:
    cards.pop()
    if len(cards) == 1:
        break
    cards.appendleft(cards.pop())

print(*cards)