'''
1. 가장높은곳과 가장 낮은곳을 구한뒤 차이 d 구하기
2. d가 k 이하인 곳만 착륙이 가능해짐
    - 1번조건
3. 본체가 위치한 칸은 가장 낮은칸 이거나 가장낮은칸보다 h 높은곳
    - 2번조건

'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K, H = map(int, input().split())
    land_arr = [list(map(int,input().split())) for _ in range(N)]

    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    count = 0

    # 주변이 8방향이 되지 않는다면 착륙 X
    for i in range(1,N-1):  # 세로로 이동
        for j in range(1,M-1): # 가로로 이동

            temp = []
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                # 8방향 탐색
                if 0 <= nx < N and 0 <= ny < M:
                    temp.append(land_arr[nx][ny])

            max_high = max(temp)    # 최고높이 찾기
            min_high = min(temp)    # 최저높이 찾기
            d = max_high - min_high # 최고와 최저의 높이차이
            e = land_arr[i][j] - min_high   # 현재위치와 최저높이의 높이차이

            # 현재위치가 최저높이보다 낮으면 착륙 X
            if land_arr[i][j] < min_high:
                continue
            else:
                if d <= K:
                    # 현재위치가 최저높이보다 같거나 높고 현재위치에서 최저높이의 차이가 H 보다 낮거나 같을때
                    if land_arr[i][j] >= min_high and e <= H :
                        count += 1

    print(f'#{tc}',count)