# 상수

def reve(num):
    reve_num = ''
    while num > 0:
        reve_num += str(num % 10)
        num //= 10
    
    return int(reve_num)

A, B = map(int, input().split())

if reve(A) > reve(B):
    print(reve(A))
else:
    print(reve(B))