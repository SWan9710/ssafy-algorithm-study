import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1,test_case+1):

    N = int(input())
    arr =[[0]*N for _ in range(N)]              # [0]으로 구성된 N*N배열 생성

    count = 1                                   # 배열에 채워 넣을 숫자의 초기값
    row = 0                                     # 가로 = i의 시작값을 바꿔주기 위해 지정
    column = 1                                  # 세로 = j의 시작값

    for num in range(N):                        # 배열의 길이만큼 반복하며 채워주기

        # 가로 한줄 채우기
        for i in range(num,N):                  # i값이 계속 바뀌어야 하기 때문에 시작 위치를 num으로 지정
            if arr[row][i] != 0:                # 예를들어 0,0이 0이 아니라 값이 들어 있다면 그냥 넘김
                continue
            arr[row][i] += count                # 값이 없다면 count값 즉 1을 채워줌
            count += 1                          # 카운트 값을 계속 증가시켜줌

        # 세로 한줄 채우기
        for i in range(num,N):                  # 세로의 시작값 마찬가지
            if arr[i][N-column] != 0:           # 0,2 부터 채워줄거기 때문에 N에서 column 값을 빼줌
                continue                        # 해당값이 0이 아닌 다른 숫자면 넘김
            arr[i][N-column] += count           # 아닐경우 0,2부터 1,2 2,2 에 count를 채워줌
            count += 1

        # 바닥줄 채우기
        for i in range(N-1-num,-1,-1):          # 바닥줄은 2,2부터 2,0까지 가야하기 때문에 N에서 num값을 빼주고 거기에 1을 빼서 에러 안나게 해줌
            if arr[N-column][i] != 0:           # 2-0,2 가 0이면 값을 채워주고 아닐경우 그냥 넘김
                continue
            arr[N-column][i] += count
            count += 1

        # 위로 채우기
        for i in range(N-1-num,-1,-1):          # 2,0 부터 0,0 까지 값을 채워줘야 함
            if arr[i][row] != 0:                # 2,0에 0이 아닐경우 그냥 넘김
                continue
            arr[i][row] += count                # 2,0 값이 0이면 count를 넣고 count는 계속 증가
            count += 1
        row += 1                                # 제일위에 있는 num 반복문이 1번 끝났을때
        column += 1
                                                # index 값이 계속 바뀌어야 하기때문에
                                                # row 와 column값을 1씩 index 값들이 대각선 안쪽으로 들어갈 수 있게 해줌
    print(f'#{tc}')                             # 이후의 결과 출력
    for result in arr:
        print(*result)