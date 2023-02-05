T = int(input())

for t in range(T):
    num, t_str = input().split()
    number = int(num)
    ans_str = ""
    for i in range(len(t_str)):
        ans_str += f'{t_str[i]*number}'
    print(ans_str)


# 문자열을 인덱스 차례대로 돌린다
# 해당문자*num 을 ans_str에 추가해서 문자열을 만든다.

# end = ""사용해서 문자를 붙였더니 테스트케이스 전부가 붙어서 오류가 남.