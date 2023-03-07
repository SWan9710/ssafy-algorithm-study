n = int(input())

t = list(map(int, input().split()))

t.sort(reverse=True)
day = []
for i in range(n):
    day.append(t[i]+i+1)

print(max(day) + 1)
