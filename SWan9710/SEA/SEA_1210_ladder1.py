import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    ladder_arr = []
    for i in range(100):
        ladder_arr.append(list(map(int, input().split())))

    x = 0
    for i in range(100):
        if ladder_arr[99][i] == 2:
            x = i
    y = 99
    # 배열이 100 * 100 이므로 최대 깊이는 ladder_arr[99]

    # 고려사항
    # 1. 오른쪽에 1이 오는 경우
    # 2. 왼쪽에 1이 오는 경우
    # 3. 양쪽모두 0인 경우
    # 4. 양쪽 동시에 사다리가 오지 않음
    while True:
        # 오른쪽이 1이어서 오른쪽으로 이동
        if x < 99 and ladder_arr[y][x+1] == 1:          # 현재의 x 는 56인데 99가 넘지않는 선(배열의 크기)에서 오른쪽이 1인 경우
            while x < 99 and ladder_arr[y][x+1] == 1:   # x값이 99 미만이고 [99][57] <= 오른쪽으로 1 증가한게 1이면
                x += 1                                  # 오른쪽으로 이동 하기 위해 1 증가
            else:                                       # 오른쪽에 0이 오는 경우 사다리의 가로가 끝난 경우 위로 가야함
                y -= 1                                  # y값을 1 줄여서 98로 만들어줌

        # 왼쪽이 1이어서 왼쪽으로 이동
        elif x > 0 and ladder_arr[y][x-1] == 1:         # x 값이 0이 아니고 56에서 -1 해준 55가 1인 경우 사다리의 가로가 왼쪽에 있는 경우
            while x > 0 and ladder_arr[y][x-1] == 1:    # 왼쪽으로 이동할건데 x값이 0이 아니고 인덱스 값이 1일때 즉 왼쪽으로 사다리가 끝날때까지
                x -= 1                                  # 왼쪽으로 이동하기 위해 1씩 감소
            else:                                       # 왼쪽 인덱스 값이 0이 온 경우 사다리의 왼쪽이 끝났을 때
                y -= 1                                  # y 값을 1 감소해서 1칸 올려줌

        #양쪽 다 0이라서 위로만 이동하는 경우
        else:                                           # 위의 조건을 모두 만족 하지 못하는 경우
            y -= 1                                      # y값을 1빼줘서 위로 올라가줌

        # y값이 0이 되면 사다리를 다 올라간 경우 더이상 올라갈 사다리가 없기에 정지해줌
        if y == 0:
            break
    print(f'#{tc} {x}')                                 # 그때 x값이 x의 출발점
