word = input()
len_word = len(word)
candidate = []

for i in range(1,len_word-1):
    for j in range(1,len_word-i):
        a = ''.join(reversed(word[0:i]))
        b = ''.join(reversed(word[i:i+j]))
        c = ''.join(reversed(word[i+j:]))
        candidate.append(a+b+c)

print(sorted(candidate)[0])