X = int(input())
n = 1

while X>n:
    X -= n
    n += 1

numer = X
denomi = n - X + 1

if n % 2:
    temp = numer
    numer = denomi
    denomi = temp

print(f'{numer}/{denomi}')