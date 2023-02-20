import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    size, pizza = map(int, input().split())
    arr = list(map(int, input().split()))
    idx_arr = [0] * len(arr)

    # 입력받은 치즈의 배열만큼 인덱스 배열 만들기
    for i in range(len(arr)):
        idx_arr[i] = i
    # new_arr 은 기존 배열의 시작에서 화덕의size 만큼 가져와서 화덕에 넣어줌
    # 그때 idx배열도 똑같이 새로 만들어줌
    new_arr = []
    new_idx = []
    for i in range(size):
        new_arr.append(arr.pop(0))
        new_idx.append(idx_arr.pop(0))
    # 위의 반복문을 돌면 arr 과 idx_arr 은 size만큼 빠지고 남은 배열 즉 대기피자가 되는거

    # 화덕에 피자가 1개가 남을때까지 돌릴거니까 현재 화덕에 남아있는 피자의 갯수가 1이 될때까지
    # 반복문을 실행해 줄거
    while len(new_arr) != 1:
        # 치즈와 idx를 현재의 피자와 배열에서 각각 뽑아서 할당
        c = new_arr.pop(0)
        idx = new_idx.pop(0)

        # 치즈는 피자가 한바퀴 돌때마다 절반씩 녹으니까 //2 해줌
        c //= 2

        # 치즈가 다 녹았을 때
        if c == 0:
            # 남은 대기피자가 있다면
            if arr:
                # 대기피자를 화덕에 넣어주고 배열도 똑같이 해줌
                new_arr.append(arr.pop(0))
                new_idx.append(idx_arr.pop(0))
            # 남은 대기 피자가 없다면 아무것도 안할 거니까 작성 안해줌
        # 치즈가 덜 녹았을때
        else:
            # 현재 화덕의 마지막에 현재의 피자를 넣어줌
            new_arr.append(c)
            new_idx.append(idx)

    print(f'#{tc}',int(*new_idx)+1)
