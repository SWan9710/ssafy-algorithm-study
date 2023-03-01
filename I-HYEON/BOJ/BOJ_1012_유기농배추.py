T = int(input())

for _ in range(T):
    M,N,K = map(int,input().split())
    cabbages = []
    for _ in range(K):
        i,j = map(int,input().split())
        cabbages.append((i,j))
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    checked = []
    cnt = 0

    for cabbage in cabbages:  # 각 좌표를 순회하면서 너비탐색할 예정
        if cabbage in checked:  # 이미 체크한 좌표면 너비탐색할 필요없이 넘어감
            continue
        else:
            checked.append(cabbage)  #  먼저 좌표에 확인 표시를 하고
            Q = [cabbage]  # 큐를 만들어 좌표를 넣음
            while Q:  # 큐에 좌표가 있는 한 계속 반복
                now = Q.pop(0)
                for k in range(4):  # 인접리스트 대신 델타 탐색
                    ni = now[0] + di[k]
                    nj = now[1] + dj[k]
                    if not (ni,nj) in checked and (ni,nj) in cabbages:
                        checked.append((ni,nj))
                        Q.append((ni,nj))
            cnt += 1

    print(cnt)