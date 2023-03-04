import sys
sys.stdin = open('input.txt')

while True:
    ttt = sys.stdin.readline().strip()
    # 종료조건
    # 가로검사 1,2,3 / 4,5,6 / 7,8,9
    # 세로검사 1,4,7 / 2,5,8 / 3,6,9
    # 대각선검사 1,5,9/ 7,5,3
    if ttt == 'end':
        break
    result = []
    for i in range(3):
        if ttt[i*3:i*3+3] == 'XXX' or ttt[i*3:i*3+3] == 'OOO':
            result.append(1)
    if len(result) == 1:
        print('valid')
    else:
        print('invalid')

