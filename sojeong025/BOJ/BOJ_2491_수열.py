import sys
sys.stdin = open('input.txt')

N = int(input())
number = list(map(int, input().split()))

count_lst = []
count1 = 1
count2 = 1
for i in range(len(number)-1):
    if number[i] <= number[i+1]:
        count1 += 1
    elif number[i] > number[i+1]:
        count_lst.append(count1)
        count1 = 1
count_lst.append(count1)

for i in range(len(number)-1):
    if number[i] >= number[i+1]:
        count2 += 1
    elif number[i] < number[i+1]:
        count_lst.append(count2)
        count2 = 1
count_lst.append(count2)

print(count_lst)
print(max(count_lst))
