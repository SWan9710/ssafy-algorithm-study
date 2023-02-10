word = input()
alp = list('abcdefghijklmnopqrstuvwxyz')

for i in alp:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print('-1', end=' ')

