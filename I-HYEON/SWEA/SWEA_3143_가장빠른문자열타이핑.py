T = int(input())
 
for tc in range(T):
    whole, part = map(lambda x:list(x),input().split())
    N = len(whole)
    M = len(part)
 
    cnt = 0
    i = 0
    j = 0
    while i<N and j<M:
        if whole[i] == part[j]:
            i += 1
            j += 1
        else:
            i = i-j+1
            j = 0
 
        if j == M:
            cnt += 1
            j = 0
             
    ans = N - cnt*M +cnt
 
    print(f'#{tc+1} {ans}')