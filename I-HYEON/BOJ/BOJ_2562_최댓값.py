max_1 = 0

for i in range(9):
    num = int(input())
    if max_1 < num:
        
        max_1 = num
        ans = i+1

print(max_1)
print(ans)