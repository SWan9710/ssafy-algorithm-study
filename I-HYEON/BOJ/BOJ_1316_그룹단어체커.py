#문자열을 입력받는다.
#문자열의 첫번째 문자가 담긴 리스트를 하나 생성한다.
#문자열을 두번째부터 끝까지 돌면서, 직전의 문자와 같으면 패스, 직전의 문자와 다르면 리스트에 추가한다.
#이 반복이 끝나면 중복이 제거된 문자열 리스트가 생성된다.
#if문으로 리스트 길이와 셋길이 가 다르면 그룹문자가 아니고, 같으면 그룹문자이다.

T = int(input())
cnt = 0
for t in range(T):
    t_str = input()
    t_list = [t_str[0]]
    for i in range(1,len(t_str)):
        if not t_str[i-1] == t_str[i]:
            t_list.append(t_str[i])
        else:
            pass
    
    if len(t_list) == len(set(t_list)):
        cnt += 1
    else:
        pass

print(cnt)