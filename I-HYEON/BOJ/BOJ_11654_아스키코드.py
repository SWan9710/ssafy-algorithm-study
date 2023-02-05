fruits = 'apple,rottenBanana,apple,RoTTenorange,Orange'
#모든 요소 소문자화해서 리스트로 만들기
fruits_list = list(map(lambda x:x.lower(),fruits.split(',')))
#왼쪽에 rotten문자열이 들어가 있으면 제거해서 빈 리스트에 추가

print(fruits_list)
ans = []
for i in range(len(fruits_list)):
    if 'rotten' in fruits_list[i] :
        ans.append(fruits_list[i].lstrip('rotten'))
    else:
        ans.append(fruits_list[i])

print(ans)

# print(fruits_list[0])
# print(fruits_list[1])
# print(fruits_list[0].lstrip('rotten'))
# print(fruits_list[1].lstrip('rotten'))