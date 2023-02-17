# N = 5이상 15이하
# M = 2이상 N 이하
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result_arr = []
    # print(arr)
    for i in range(N-M+1):    # N =5  # M = 2
        for j in range(N-M+1):
            result = 0
            for k in range(i,i+M):
                for s in range(j,j+M):
                    result += arr[k][s]
            result_arr.append(result)
    print(f'#{tc}',max(result_arr))