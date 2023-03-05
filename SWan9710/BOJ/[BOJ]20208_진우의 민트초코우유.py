'''
우유의 좌표값에서 집의 좌표값을 뺏을때
그 거리가 현재의 체력보다 적거나 같다면
백트래킹을 이용하여 재귀함수를 불러와야 함

문제를 풀면서 중반까지는 구성을 완료하였는데 우유를 마신 횟수를 어떻게 반환해야 할지 못찾음
소정이와 은경씨의 코드를 참고하여 DFS내 if문을 작성하긴 했는데 왜 저렇게 돌아가는지 아직 잘 모르겠음
'''


import sys
sys.stdin=open('input.txt')

def DFS(x, y, M, count):
    global result

    for sx, sy in milk:
        # 아직 마시지 않은 우유일때
        if arr[sx][sy] == 2:
            # ex) 집의 좌표 6, 3 / 우유의 좌표 7, 4 일때
            # 좌표값의 차는 1, 1 => 이동거리는 1+1 로 총 2가됨
            length = abs(x - sx) + abs(y - sy)
            # 우유의 좌표에서 집까지의 거리를 뺏을때 그게 체력보다 많을경우
            if length <= M:
                # 현재 좌표에 있는 우유는 마셨기 때문에 0으로 바꿔주기
                arr[sx][sy] = 0
                # 현재 체력에서 length를 빼주고, 우유를 마셨으니 H 만큼 더해줌
                # 우유를 마신 횟수 역시 +1
                DFS(sx, sy, M + H - length, count + 1)
                # 재귀가 끝났을때 다음탐색을 위해서 우유값을 복구해주기
                arr[sx][sy] = 2

    if abs(x - hx) + abs(y - hy) <= M:
        result = max(result, count)

N, M, H = map(int, input().split())

# 지도
arr = [list(map(int, input().split())) for _ in range(N)]

# 민초우유가 있는 좌표값을 리스트로 저장
milk = []
result = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            hx, hy = i, j
        if arr[i][j] == 2:
            milk.append([i, j])

DFS(hx, hy, M, 0)
print(result)