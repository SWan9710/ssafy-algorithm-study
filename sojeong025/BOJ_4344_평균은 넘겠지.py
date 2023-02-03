# 평균은 넘겠지
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력

# import sys
# sys.stidin = open("input.txt")

C= int(input())

for tc in range(1,C+1):
    grade=list(map(int, input().split()))
    avg=sum(grade[1:])/grade[0]

    count=0
    for i in grade[1:]:
        if i > avg :
            count += 1
        
    rate = (count / grade[0]) * 100

    print(f'{rate:.3f}%')

    
    
    