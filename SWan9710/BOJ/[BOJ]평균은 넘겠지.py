c = int(input())

for i in range(c):
    arr = []
    x = input().split()
    result = 0
    avg = 0
    for j in range(1,len(x)):
        result += int(x[j])
    avg = result/int(x[0])

    count = 0
    for k in range(1, len(x)):
        if int(x[k]) > avg:
            count += 1
    total_result = ((100 / (len(x)-1) * count))
    print('%.3f'%total_result+'%')
