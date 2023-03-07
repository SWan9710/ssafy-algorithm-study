T = int(input())

for tc in range(T):
    H, W, N = map(int,input().split())

    if N % H == 0:
        floor = H
        room = format(N // H, '02')
    else:
        floor = N % H
        room = format(N // H + 1, '02')

    print(str(floor)+str(room))