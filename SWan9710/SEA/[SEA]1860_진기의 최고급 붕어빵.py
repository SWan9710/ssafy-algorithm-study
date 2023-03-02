import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    # N 사람수 / M 걸리는 시간 / K 만드는 갯수
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()

    for i in range(N):
        result = (people[i] // M) * K - (i+1)
        if result < 0:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')