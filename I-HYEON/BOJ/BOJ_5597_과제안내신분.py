#총 28개의 입력값이 있고 총 1-30이어야 하는데 그 중 빠진
#숫자를 구해야함
#for 문을 돌면서 받아온 input값을 리스트에서 빼는 방식으로
#풀 수 있을까?

import sys
mylist = list(range(1,31))

for i in range(28):
    mylist.remove(int(sys.stdin.readline()))

print(mylist[0])
print(mylist[1])