import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1,test_case+1):
    sdoku_arr = []

    #스도쿠 가져오기
    for i in range((tc*9)-9,tc*9):
        sdoku = list(map(int, input().split()))
        sdoku_arr.append((sdoku))
    # print(sdoku_arr)

    # 스도쿠 90도 회전
    # 전치행렬이다.
    rotation_sdoku = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            rotation_sdoku[i][j] = sdoku_arr[j][i]

    # 스도쿠 3칸씩 가져오기
    block_sdoku = [[0] * 9 for _ in range(0)]
    for i in range(1, 10, 3):  # i >> 1, 4, 7
        for j in range(1, 10, 3):  # j >> 1, 4, 7

            # 블럭으로 가져오는 스도쿠를 저장할 공간
            temp_sdoku = []

            for k in range(-1, 2):  # k >> -1, 0, 1                 # 0,0 / 0,1 / 0,2
                for m in range(-1, 2):  # m >> -1, 0, 1             # 1,0 / 1,1 / 1,2
                                                                    # 2,0 / 2,1 / 2,2
                    # 제일먼저 j값이 바뀌고 그다음 i 값이 바뀜
                    temp_sdoku.append(sdoku_arr[i + k][j + m])
            block_sdoku.append((temp_sdoku))

    #스도쿠 가로줄 중복 검사하기
    duplication = 0
    for i in range(9):
        if len(set(sdoku_arr[i])) != 9:
            duplication += 1
            break
            # 리스트 전체의 값이 45가 아닐때 중복을 늘린다.
            # 5 5 5  5 5 5  5 5 5 >> 반례가 있다,,,,

    # 스도쿠 세로줄 중복 검사하기
        if len(set(rotation_sdoku[i])) != 9:
            duplication += 1
            break

    # 블럭스도쿠 중복 검사
        if len(set(block_sdoku[i])) != 9:
            duplication += 1
            break

    if duplication == 0:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)