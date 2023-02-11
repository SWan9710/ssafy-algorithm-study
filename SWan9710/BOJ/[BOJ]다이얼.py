# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 
# 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.
# 숫자 1을 걸려면 총 2초가 필요하다.
# 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

num_list = ['1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

words = input()
words = ''.join(words)
words = list(words)

count = len(words)
for i in range(len(words)):
    for j in range(len(num_list)):
        if words[i] in num_list[j]:
            count += num_list.index(num_list[j])+1
print(count)


