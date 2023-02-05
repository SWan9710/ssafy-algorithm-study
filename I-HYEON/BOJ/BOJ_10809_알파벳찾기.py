from string import ascii_lowercase

al_li = list(ascii_lowercase)

#문자열을 입력받아, 리스트로 만든다
#빈리스트를 만든다.
# 알파벳리스트를 차례대로 돈다. 예를 들어 a를 갖고온다
# 문자열리스트를 돈다.
# 만약 a랑 같은 알파벳이면 그때 인덱스를 빈리스트에 추가하고,
# 문자열리스트를 도는 행위를 그만두고, flag = True,다음 알파벳으로 넘어간다.
# 만약 a랑 같은 알파벳이 아니면 flag = False, continue 한다.
# 문자열이 도는 포문이 끝났을때 flag = False면 -1을 빈리스트에 추가한다.
# 리스트를 반환한다.

tc = list(input())

ans_list = []

for i in al_li:
    for j in range(len(tc)):
        if i == tc[j]:
            ans_list.append(j)
            flag = True
            break
        else:
            flag = False
            continue
    if flag == False:
        ans_list.append('-1')
    else:
        pass

print(*ans_list)