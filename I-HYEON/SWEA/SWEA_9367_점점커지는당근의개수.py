T = int(input())
for t in range(T):
    N = int(input())
    Carrots = list(map(int,input().split()))
 
    temp = []
    cnt = 1
    for i in range(1,N):
        if Carrots[i] == Carrots[i-1] + 1:
            cnt +=1
        else:
            temp.append(cnt)
            cnt = 1
        temp.append(cnt)
 
    ans = max(temp)
    print(f'#{t+1} {ans}')