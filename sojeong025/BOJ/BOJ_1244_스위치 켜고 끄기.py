'''
구현 방법 아이디어
1. 조건문을 통해 student_switch 의 첫번째 인덱스 값에 따라 두 가지 방향성 제시
    1-1. 남자면 switch 인덱스 + 1 이 받은 수의 배수이면 상태 바꾸기
    1-2. 여자면 switch 인덱스 + 1 이 받은 수 같은 번호를 기준으로
'''

import sys
sys.stdin = open('input.txt')

N = int(input())
switch = list(map(int, input().split()))
student = int(input())
for i in range(student):
    student_switch = list(map(int, input().split()))

    # 남학생일 때
    if student_switch[0] == 1:
        for j in range(len(switch)):
            if (j + 1) % student_switch[1] == 0:
                switch[j] = int(not switch[j])

    # 여학생일 때
    else:
        for j in range(len(switch)):
            if (j + 1) == student_switch[1]:
                next = j + 1
                pre = j - 1
                # 남학생일 때 바뀐거 다시 재설정
                switch[j] = int(not switch[j])
                while True:
                    if next < len(switch) and pre >= 0:
                        # 양쪽이 대칭이면 양쪽 값을 반대로
                        if switch[pre] == switch[next]:
                            switch[pre] = int(not switch[pre])
                            switch[next] = int(not switch[next])
                        else:
                            break
                    else:
                        break
                    pre -= 1
                    next += 1
# 20개씩 출력
for num in range(0, N, 20):
    print(*switch[num:num+20])



