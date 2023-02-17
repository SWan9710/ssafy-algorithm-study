import sys

N = int(sys.stdin.readline())

#카운팅할수있도록 빈 배열을 생성
temp = [0 for i in range(10001)]

#숫자를 받아오면서 동시에 카운팅
for i in range(N):
    temp[int(sys.stdin.readline())] += 1
#카운팅 배열을 돌면서 순서대로 출력
for i in range(10001):
    for j in range(temp[i]):
        print (i)