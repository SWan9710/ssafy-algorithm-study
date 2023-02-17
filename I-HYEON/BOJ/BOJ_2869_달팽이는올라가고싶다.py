A,B,V = map(int,input().split())


if (V-A)%(A-B) == 0:
    ans = (V-A)//(A-B)
else:
    ans = (V-A)//(A-B)+1

result = ans + 1

print(result)