number = []
for i in range(5):
    number.append(int(input()))

number.sort()
print(int(sum(number)/5))
print(number[2])