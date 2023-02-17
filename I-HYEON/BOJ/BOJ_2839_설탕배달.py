N = int(input())

temp = N//5
ans = -1
while temp>=0:
    if (N - (5 * temp)) % 3 == 0:
        ans = temp + (N - (5 * temp))//3
        break

    temp -= 1

print(ans)