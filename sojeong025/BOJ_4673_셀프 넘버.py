def self_number(num):
    self_num=num
    while num != 0:
        # 오른쪽 끝 숫자를 더함
        self_num += num % 10
        # 오른쪽 끝 숫자를 삭제
        num //= 10
    return self_num

answer=[]
for i in range(1,10001):
    answer.append(self_number(i))
    # 생성자가 없는 것이 셀프 넘버
    if i not in answer:
        print(i)