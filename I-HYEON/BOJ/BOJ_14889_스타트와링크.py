def comb(arr, n):  # 조합 구하는 함수
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)

    return result

def cal_stats(arr):  # 팀의 능력치 구하는 함수
    sum = 0
    for i in comb(arr,2):
        sum += stats[i[0]-1][i[1]-1]
        sum += stats[i[1]-1][i[0]-1]

    return sum

N = int(input())  # 총 인원
people = [i for i in range(1,N+1)]  # 총 인원 담긴 리스트
stats = [list(map(int,input().split()))for _ in range(N)]  # 능력치 계산 배열

start = comb(people, N//2)  # 스타트팀 조합이 담긴 리스트
link = [[x for x in people if x not in s] for s in start]  # 링크팀 조합이 담긴 리스트

ans = 200000
for i,j in zip(start,link):
    if ans > abs(cal_stats(i) - cal_stats(j)):
        ans = abs(cal_stats(i) - cal_stats(j))

print(ans)