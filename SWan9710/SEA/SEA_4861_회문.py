import sys
sys.stdin = open('input.txt')

def verses(arr,word_len,size):
    reverse_word = []               # 문자를 거꾸로 넣을 배열
    new_word = []                   # 문자를 앞에서 부터 넣을 배열

    # 배열을 행우선조회를 통해 문자의 길이만큼 반복문을 돌림

    for x in range(size):                                       # 만약 배열의 길이가 20일때
        for i in range(size - word_len + 1):                    # 20 - 문자의길이(13) 에 자기자신 포함 +1
            if i == 0:                                          # 문자를 거꾸로 넣을때 첫번째 값을 거꾸로 넣을때는
                reverse_word.append((arr[x][word_len - 1::-1])) # 문자의 길이 13부터 0번째 값이므로 끝까지 넣어줌
            else:
                reverse_word.append(arr[x][word_len - 1 + i:i - 1:-1])  # i가 1이 되면 문자의 길이 +i 부터 i번째 값까지 넣어줌

    # 배열을 앞에서 부터 넣어줌
    for x in range(size):                               # 만약 20일때
        for i in range(size - word_len + 1):            # 20 - 13 + 1 까지 총 7번 0,1,2,3,4,5,6,7 까지 넣어줌
            new_word.append(arr[x][i:i + word_len])     # 앞에서 부터 끊어서 하나씩 넣어줌

    # 배열이 같은지 확인하기
    for i in range(len(new_word)):                      # 앞에서부터 넣은 값과 뒤에서 부터 넣은 값이 똑같다면
        if reverse_word[i] == new_word[i]:              # 해당하는 문자열 출력
            print(f'#{tc} ',*reverse_word[i],sep='')

    return reverse_word, new_word

test_case = int(input())
for tc in range(1, test_case+1):
    arr_size, word_length = map(int, input().split())

    row_arr = []    # 가로배열
    col_arr = []    # 세로배열

    # 가로배열을 2차원 형태의 배열로 받아서 만들어줌
    for x in range(arr_size):
        input_word = list(input())
        row_arr.append(input_word)

    # 세로배열을 2차원 형태의 배열로 만들어주기
    for i in range(arr_size):
        new_arr = []
        for j in range(arr_size):           # 가로배열에서 앞글자만 따서 1차원 배열 new_arr에 넣어줌
            new_arr.append(row_arr[j][i])
        col_arr.append(new_arr)             # 이후 그 배열 자체를 다시 배열에 넣어서 2차원 배열로 만들어줌

    verses(row_arr,word_length,arr_size)    # 가로배열 검사
    verses(col_arr,word_length,arr_size)    # 세로배열 검사
