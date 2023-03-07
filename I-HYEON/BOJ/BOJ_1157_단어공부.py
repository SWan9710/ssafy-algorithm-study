#인풋을 입력받는다
#전체 문자열을 모두 대문자로 바꾼후 리스트에 담는다
#set을 사용해서 중복을 제거한 리스트를 만든다.
#빈리스트를 만든다.
#중복을 제거한 리스트를 돈다.
    #cnt에 0을 할당한다.
    #문자열(대문자)리스트를 돈다.
    #만약, 이문자가 문자열의문자와 일치하면 cnt+=1을한다.
    #문자열을 도는 for문이 끝나면 cnt를 빈리스트에 추가한다.
#count 메서드를 이용, 만약 max값이 2 이상이면 '?'를 반환하고
#1이라면 set[해당인덱스]를 반환한다.

str_upp = list(input().upper())
al_list = list(set(str_upp))

al_num = []
for i in al_list :
    cnt = 0
    for j in str_upp:
        if i == j:
            cnt += 1
    al_num.append(cnt)

if al_num.count(max(al_num)) == 1 :
    print(al_list[al_num.index(max(al_num))])
else:
    print('?')