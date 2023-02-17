G = list(input())
idx = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

num = []
for i in range(len(G)):
    for j in range(len(idx)):
        if G[i] in idx[j]:
            number = j+3
            break
        else:
            pass
    num.append(number)

print(sum(num))