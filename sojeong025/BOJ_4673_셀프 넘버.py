def self_number(num):

    self_num=num
    while num != 0:
        self_num += num % 10
        num //= 10
    return self_num

answer=[]
for i in range(1,10001):
    