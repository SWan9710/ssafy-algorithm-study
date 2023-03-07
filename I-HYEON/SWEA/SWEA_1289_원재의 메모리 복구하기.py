T = int(input())

for tc in range(1, T + 1):
    bit = input()
    N = int(bit,2)
    now = 0  # 현상태를 0으로 초기화

    cnt = 0
    for i in range(len(bit),-1,-1):  # bit의 길이만큼 검사
        if N & (1 << i):  # i 번째 비트가 1이다?
            if now == 1:  # 현상태도 1이다?
                pass
            elif now == 0:  # 현상태가 0이다?
                cnt +=1  # 카운팅
                now = 1  # 상태 변환
        else:  # i 번째 비트가 0이다?
            if now == 0:  # 현 상태도 1이다?
                pass
            elif now == 1:  # 현 상태가 0이다?
                cnt += 1  # 카운팅
                now = 0  # 상태 변환

    print(f'#{tc}',cnt)