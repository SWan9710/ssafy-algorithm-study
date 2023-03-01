N = int(input())

n_lst = []
for i in range(N):
    n_lst.append(int(input()))

n_lst.sort()
for i in range(len(n_lst)):
    print(n_lst[i])