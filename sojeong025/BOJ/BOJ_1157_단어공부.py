word = input().upper()

# 알파벳으로 구현된 새 리스트를 만들고
# 그 리스트의 인덱스를 돌며 word가 일치하면 +1 씩 해준다
# 그 결과값이 담긴 리스트에서 가장 최고를 찾고
# 그 값이 2이상이면 ? 출력 하나면 알파벳 출력

alp = list(set(word))

count_lst = []
for i in alp:
    count = word.count(i)
    count_lst.append(count)

if count_lst.count(max(count_lst)) > 1:
    print('?')
else: 
    print(alp[(count_lst.index(max(count_lst)))])