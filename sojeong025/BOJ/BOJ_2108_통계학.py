import sys
from collections import Counter
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

# 1. 산술평균 - 소수점 이하 첫째 자리에서 반올림한 값 출력
print(round(sum(li)/n))

# 2. 중앙값 출력 (n은 홀수)
li.sort()
print(li[n//2])

# 3. 최빈값
count_li = Counter(li).most_common()
if len(count_li) > 1 and count_li[0][1] == count_li[1][1]:
    print(count_li[1][0])
else:
    print(count_li[0][0])

# 4. 범위
print(max(li)-min(li))


