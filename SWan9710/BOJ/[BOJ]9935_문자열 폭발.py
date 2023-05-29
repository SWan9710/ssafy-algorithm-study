'''
replace로 했더니 시간초과 났음
stack으로 바꿔서 문자열 단순비교로 실시

입력받은 word의 문자를 하나씩 stack에 넣어주는데
넣은 문자가 폭발 문자열의 마지막 문자와 같은경우
해당 문자의 위치부터 끝까지 비교해서 그 글자가 폭발문자열과 같은경우 stack에서 제거해주기
'''
import sys
input = sys.stdin.readline

word = input().strip()
bomb = list(input().strip())

stack = []
# 폭발 문자열의 길이
length = len(bomb)

# 폭발 문자열의 마지막 문자
last_bomb = bomb[-1]

# word의 1글자씩 stack에 넣어주기
for char in word:
    stack.append(char)
    # 입력받은 char이 폭발 문자열의 마지막 글자와 같고
    # 해당 문자 위치부터 끝까지 비교해서 글자가 폭발 문자열과 같은경우 제거해주기
    # -length 해주는 이유?
    '''
    폭발 문자열의 길이는 입력받을때 정해지는데 입력 받은 폭발 문자열의 길이가 2인 경우 -2를 해주면
    stack에 들어간 문자에서 뒤에서 2번째를 보게됨 즉 폭발 문자열의 시작위치를 보는거
    거기부터 끝까지 => 폭발 문자열이 되는경우 stack에서 폭발 문자열을 제거 해주면 됨
    '''
    if char == last_bomb and stack[-length:] == bomb:
        # 폭발 문자열의 길이만큼 반복문 실행
        # 스택의 뒤에서부터 폭발 문자열의 길이만큼 제거
        for _ in range(length):
            stack.pop()

# 결과출력
if stack:
    print(''.join(stack))
else:
    print('FRULA')