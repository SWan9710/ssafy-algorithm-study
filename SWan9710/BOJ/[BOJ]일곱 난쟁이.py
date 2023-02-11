arr = [int(input()) for i in range(9)]

# 종료조건 설정해주기
count = 0
over = sum(arr)-100                     # 난쟁이의 키 총합에서 100을 뺀값이 오버되는 키
for i in range(9):                      # i = 0 ~ 9
    for j in range(9):                  # j = 0 ~ 9
        if i == j:                      # 자기자신은 비교하지 않는 코드
            continue
        if arr[i] + arr[j] == over:     # arr의 i번째 값과 j번째 값이 over값과 같다면
            if i > j:                   # i값과 j값의 크기를 비교
                arr.pop(i)              # i 가 j보다 크다면 arr의 i번째 값을 없애주면 리스트의 인덱스가 1씩 감소
                arr.pop(j+1)            # 해당 인덱스 값에 1을 더해줘서 조건에 맞는 값을 빼주기
                                        # remove 이용해서 값 자체를 제거해주기
            else:
                arr.pop(i)
                arr.pop(j-1)
            count = 1                   # 종료조건으로 1설정해주고
            break                       # 해당조건 다 맞으면 멈추기        
    if count == 1:                      # 종료조건이 맞으면 for i 번째를 더이상 실행하지 않고 종료
        break
arr.sort()                              # 리스트 다시 정렬하고 출력하기
for i in arr:
    print(i)
