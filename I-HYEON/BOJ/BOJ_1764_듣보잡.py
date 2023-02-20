N,M = map(int,input().split())

N_li = []
M_li = []
for i in range(N):
    N_li.append(input())

for i in range(M):
    M_li.append(input())

no_hear = set(N_li)
no_see = set(M_li)

print(len(no_hear & no_see))
for i in sorted(no_hear & no_see):
    print (i)