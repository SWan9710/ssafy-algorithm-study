import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    # 1 => N극 2=> S극
    # 교착상태의 테이블 만들기
    for i in range(N):
        for j in range(N):
            # i = 0  j = 0 N = 10
            num = 0
            while True:  # 0 + 0 < N
                if i + num + 1 < N:
                    if table[i+num][j] == 1 and table[i+num+1][j] == 0:
                        table[i+num+1][j] = 1
                        table[i+num][j] = 0

                if i - num -1 >= 0:
                    if table[i-num][j] == 2 and table[i-num-1][j] == 0:
                        table[i - num - 1][j] = 2
                        table[i - num][j] = 0

                else:
                    break
                num += 1

    # 교착상태의 갯수세기
    # 1번 아래에 2번이 있는경우만 교착상태
    count = 0
    for i in range(N-1):
        for j in range(N):
            if table[i][j] == 1:
                if table[i+1][j] == 2:
                    count += 1
    print(f'#{tc+1}',count)
