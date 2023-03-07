'''
N개의 바구니가 있다.
이 바구니들에 어떤 짓을 M번 반복할 거다.
그 어떤 짓이라는 건, 범위와 기준점이 주어지면 기준점~범위끝까지를 앞으로갖고오고 나머지를
뒤로 미루는 식으로 바구니 순서를 바꾸는 짓이다.

일단 N+1 배열을 만든다.
그리고 매번(총 M번) 시작점,끝점,기준점을 받아와서
배열의 시작점부터 끝점까지 반복하면서 해당 위치에,
기준점부터 끝점까지를 먼저넣고, 시작점부터 기준점-1까지의 원소를 넣는다.
'''
import copy

N,M = map(int,input().split())
arr = [i for i in range(N+1)]  # 바구니 번호가 인덱스 대로 담겨 있다.
for _ in range(M):
    temp = copy.deepcopy(arr)
    i,j,k = map(int,input().split())
    temp1 = list(range(i, j + 1))  # 주어진 범위(이 안을 바꿀 예정)
    temp2 = list(range(k, j + 1)) + list(range(i, k))  # 배치방식 인덱스
    for u,w in zip(temp1,temp2):
        arr[u] = temp[w]

print(*arr[1:])