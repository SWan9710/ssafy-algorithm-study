#두수를 문자열로 입력받는다
#슬라이싱으로 거꾸로된 문자열을 만들고 INT로 바꾼후
#비교한다

A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])

if A>B:
    print(A)
else:
    print(B)