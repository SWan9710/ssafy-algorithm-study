T = 10
 
def s_max(x):
    num = x[0]
    for i in x:
        if num < i:
            num = i
    return  num
 
def s_min(x):
    num = x[0]
    for i in x:
        if num > i:
            num = i
    return  num
 
for i in range(T):
    N = int(input())
    box_list = list(map(int,input().split()))
    # 834번 덤프를 실행
    for j in range(N):
        #한번 덤프할때마다 리스트를 돌면서 맥스,민 값을 갖는 인덱스를 찾아 각각 +1,-1해준다
        if s_max(box_list)-s_min(box_list) <= 1:
            break
        else:
            box_list[box_list.index(s_max(box_list))] -= 1
            box_list[box_list.index(s_min(box_list))] += 1
 
    print(f'#{i+1} {s_max(box_list) - s_min(box_list)}')