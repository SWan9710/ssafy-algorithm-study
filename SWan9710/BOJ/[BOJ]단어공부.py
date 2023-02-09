s = input()
s = s.upper()
upper_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
upper_word_arr = [0] * 26

for i in range(len(s)):
    if s[i] in upper_alphabet:
        upper_word_arr[upper_alphabet.index(s[i])] += 1

max_upp = sorted(upper_word_arr)

if max_upp[-2] == max_upp[-1]:
    print('?')
else:
    word = upper_alphabet[upper_word_arr.index(max_upp[-1])]
    print(word)
