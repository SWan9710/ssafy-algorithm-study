T = int(input())
for t in range(T):
    N = int(input())
    nums = input()
    nums_list = []
    count = [0 for i in range(10)]
    for i in nums:
        nums_list.append(int(i))
 
    for i in nums_list:
        count[i] += 1
 
    temp = []
    for i in range(len(count)):
        if count[i] == max(count):
            card_number = i
            card_count = count[i]
 
    print(f'#{t+1} {card_number} {card_count}')