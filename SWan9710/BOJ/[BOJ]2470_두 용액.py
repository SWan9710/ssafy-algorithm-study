'''
이분탐색 문제
찾아야 되는 값은 0에 가장 근접하는 값을 찾아야 함
최초 start, end 지정 -> 정렬 후의 값을 start와 end 로 지정하니 두개의 값을 더해서 저장해둠

start = 0
end = N - 1
result = abs(arr[start] + arr[end])

이때 두개의 위치를 저장
temp = [arr[start], arr[end]]

이분 탐색 실시하며 start와 end값을 초기화 시켜주는데 start가 end 보다 작은 경우 즉 배열 안에서 반복되는 경우에만 이분탐색을 실시

두개의 결과를 더했을 때 현재 저장한 result 보다 값이 더 작은 경우 > 절댓값 이 더 작다는건 0에 더 근접한다는 의미
이 두개의 값을 새롭게 result로 초기화
이 두개의 위치를 저장

그게 아닌경우에는 start와 end 의 위치를 이동
'''

N = int(input())
arr = list(sorted(map(int, input().split())))

start = 0
end = N - 1

result = abs(arr[start] + arr[end])
temp = [arr[start], arr[end]]

while start < end:
    start_val = arr[start]
    end_val = arr[end]

    total = arr[start] + arr[end]

    # 절댓값이 더 작은경우
    if abs(total) < result:
        result = abs(total)
        temp = [start_val, end_val]

        # 더 작은 이값이 0인경우 찾으려는 용액의 값을 찾았으므로 종료
        if result == 0:
            break

    # 절댓값이 더 크므로 이분탐색 실시
    if total < 0:
        start += 1
    
    else: 
        end -= 1

print(temp[0], temp[1])