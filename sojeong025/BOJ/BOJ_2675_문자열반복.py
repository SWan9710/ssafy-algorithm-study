T = int(input())

for tc in range(1, T+1):
    R, S = input().split()
    
    # 반복된 최종 문자열
    # 문자열은 *을 하면 반복되는 특징
    word = ""
    for i in S:
        word += int(R) * i
    print(word)