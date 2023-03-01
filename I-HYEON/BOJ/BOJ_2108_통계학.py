import sys
input = sys.stdin.readline

N = int(input().rstrip())

lst = []
for _ in range(N):  # N만큼 반복해서 숫자를 리스트에 받아온다.
    lst.append(int(input().rstrip()))

lst = sorted(lst)
'''
(a)산술평균 = (리스트합) / (리스트길이)
(m)중앙값 = (리스트길이를 2로 나눈 인덱스원소)
(u)최빈값 = (리스트를 셋으로 만들어서 이걸 키로하는 딕셔너리를 만듦, 그리고 갯수 세기)
(r)범위 = (최대값에서 최소값뺀거)
'''

a = sum(lst)/len(lst)  # 산술평균
m = lst[len(lst)//2]  # 중앙값
r = max(lst)-min(lst)  # 범위

mydict = {}
for i in lst:
    if not i in mydict:
        mydict[i] = 1
    else:
        mydict[i] += 1

temp = []
for k,v in mydict.items():  #  딕셔너리의 키,밸류를 반복적으로 순회하면서
    if v == max(mydict.values()):  # 밸류값이 최대값이라면
        temp.append(k)  # 전부 리스트에 담아준다

if len(temp) >= 2:  # 최빈값이 두개 이상이라면
    u = sorted(temp)[1]  # 그 중 두번째로 작은 값이 최빈값이고
else:
    u = temp[0]  # 아니면 그냥 그 하나를 최빈값으로 간주

print(round(a))
print(m)
print(u)
print(r)