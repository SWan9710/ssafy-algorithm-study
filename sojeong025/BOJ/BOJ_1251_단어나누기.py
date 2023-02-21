import sys
sys.stdin = open('input.txt')

word = input()
reverse_word = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]

        re_a, re_b, re_c = a[::-1], b[::-1], c[::-1]
        reverse_word.append("".join(re_a + re_b + re_c))

# print(reverse_word)
reverse_word = sorted(reverse_word)
# print(reverse_word)
print(reverse_word[0])