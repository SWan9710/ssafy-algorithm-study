# 크로아티아 알파벳
# ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
# 첫째 줄에 최대 100글자의 단어가 주어진다. 
# 알파벳 소문자와 '-', '='로만 이루어져 있다.

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
words = input()

for i in alphabet:
    if i in words:
        words = words.replace(i,'A')

print(len(words))

