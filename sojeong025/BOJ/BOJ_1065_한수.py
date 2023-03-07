def han(num):
    han_cnt=0
    for n in range(1, num+1):
        num_list= list(map(int, str(n)))
        # 1부터 99까지는 모두 한수
        if n < 100 :
            han_cnt += 1
        # 1000보다 작거나 같은 자연수 범위니 idx[2]까지 비교해서 cnt += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            han_cnt += 1
    return han_cnt

num = int(input())
print(han(num))
