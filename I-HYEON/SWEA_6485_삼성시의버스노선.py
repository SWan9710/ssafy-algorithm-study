T = int(input())
 
for t in range(T):
    N = int(input())
    b_range = []
    for i in range(N):
        a, b = map(int, input().split())
        b_range.append(list(range(a, b + 1)))
    b_number = int(input())
    b_stops = []
    for i in range(b_number):
        b_stops.append(int(input()))
 
    # print(N,b_range,b_number,b_stops)
 
    e = []
    for i in range(b_number):
        cnt = 0
        for j in range(N):
            if b_stops[i] in b_range[j]:
                cnt += 1
        e.append(cnt)
 
    print(f'#{t+1}',*e)