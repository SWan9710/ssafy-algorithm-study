N = int(input())    # 스위치 갯수
switch =[-1]+list(map(int, input().split()))    # 스위치 상태
people = int(input())   # 학생수
for k in range(people):
    gender, num = map(int, input().split())
    # 남 == 1,  여 == 2
    # 남학생
    if gender == 1:
        plus_num = num
        # 0 => -1을 1로 1을 0으로
        while num < N+1:
            switch[num] = abs(switch[num]-1)
            num += plus_num
    # 여학생
    elif gender == 2:
        i = 1
        switch[num] = abs(switch[num] - 1)
        while True:
            if 1 <= num-i and num+i <= N:
                if switch[num - i] == switch[num + i]:
                    switch[num - i] = abs(switch[num - i]-1)
                    switch[num + i] = abs(switch[num + i] - 1)
                else:
                    break
            else:
                break
            i += 1

for nums in range(1, N+1):
    print(switch[nums], end=' ')
    if nums % 20 == 0:
        print()