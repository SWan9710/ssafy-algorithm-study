'''
9명의 난장이 키를 리스트로 받아온다
해당 리스트의 부분집합을 모두 출력한다.
그 중 원소개수가 7개이면서, 합이 100인 리스트를 filter한다.
결과리스트를 돌려서 제일 마지막에 나오는 리스트(랜덤이니까)를 sorted로 정렬해서 출력
'''
h_list = []
for i in range(9):
    h_list.append(int(input()))

b_list = []
for i in range(1<<9):
    a_list = []
    for j in range(9):
        if i & (1<<j):
            a_list.append(h_list[j])
    b_list.append(a_list)

b_combi = list(filter(lambda x:len(x) == 7 and sum(x) == 100,b_list))
for i in range(len(b_combi)):
    ans = sorted(b_combi[i])

for i in ans:
    print(i)