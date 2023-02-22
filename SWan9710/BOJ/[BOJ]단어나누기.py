# 길이 3 이상 50 이하
word = input()
n = len(word)
word_list = []
# 1부터 단어길이 -1 까지
for i in range(1, n-1):
    for j in range(i+1, n):
        # 처음부터 i까지
        L_word = word[:i]
        # i부터 j까지
        M_word = word[i:j]
        # j부터 끝까지
        R_word = word[j:]
        result = L_word[::-1] + M_word[::-1] + R_word[::-1]
        word_list.append(result)
word_list.sort()
print(word_list[0])