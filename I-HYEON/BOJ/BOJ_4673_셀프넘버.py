def d(a):
    digit_sum = 0
    temp = a 
    while temp > 0 :
        digit_sum += temp % 10 
        temp = temp // 10 
    return a + digit_sum 

d_result = []
for i in range(1,10000):
    d_result.append(d(i))

ans = [i for i in range(1,10000)]

selfnumber = []
for i in ans:
    if not i in d_result:
        selfnumber.append(i)

for i in selfnumber:
    print(i)