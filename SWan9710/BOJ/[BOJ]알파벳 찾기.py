s = input()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

num = [-1] * len(alphabet)
for i in range(len(s)):
    if s[i] in alphabet:
        if num[alphabet.index(s[i])] != -1:
            continue
        else:
            num[alphabet.index(s[i])] = i
print(*num)