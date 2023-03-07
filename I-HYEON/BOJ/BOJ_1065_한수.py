#일의 자리수일때, 한수의 개수는 본인
#십의 자리수일때, 한수의 개수는 본인
#백의 자리수일때, 한수의 개수는?
#숫자를 str으로 만들고 int(str[1])-int(str[0])=int(str[2])-int(str[1])인지
#확인해서 맞으면 True,아니면 False을 반환하는 함수를 만든다
#숫자를 입력하면 1부터 숫자까지 돌면서 함수에 넣으면서 카운트한다.

def hansu(n):
    num = str(n)
    if n < 100:
        return True
    else:
        if int(num[1])-int(num[0]) == int(num[2])-int(num[1]):
            ans = True
        else:
            ans = False
        return ans

N = int(input())

if N < 100:
    print(N)
else:
    cnt = 0
    for i in range(1,N+1):
        if hansu(i) == True:
            cnt += 1
    print(cnt)