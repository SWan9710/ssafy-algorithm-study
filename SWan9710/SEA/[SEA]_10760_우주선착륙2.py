import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 8방향탐색
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]

    # 결과를 저장할 변수
    result = 0

    for i in range(N):
        for j in range(M):
            # i나 j값이 바뀔때마다 비교 지역이 달라지니 계속 초기화를 위해
            # k 위에 초기화
            count = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                # nx와 ny가 범위 내에 있을때
                if 0<= nx <N and 0 <= ny < M:
                    if arr[i][j] > arr[nx][ny]:
                        count += 1

            if count >= 4:
                result += 1
    print(f'#{tc}',result)