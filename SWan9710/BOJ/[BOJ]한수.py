# 한수
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

N = int(input())
count = 0   # 등차수열의 갯수를 셀 변수
if N <= 99:  # N이 100보다 큰경우
    for i in range(N):
        count += 1

arr = []
if N > 99:
    count += 99
    for i in range(100, N+1):
        arr.append(str(i))
    
    for i in range(len(arr)):
        if int(arr[i][0]) - int(arr[i][1]) == int(arr[i][1]) - int(arr[i][2]):
            count += 1
print(count)
    
    
