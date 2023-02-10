import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(test_case):

    words = input()
    length = (len(words) * 5) - (len(words) - 1)
    words_arr = [['.'] * length for _ in range(5)]

    if len(words) == 1:

        for i in range(5): # 세로길이
            if i % 2 == 0:
                for j in range(0,length,2):
                    words_arr[i][j] = '#'

            if i == 2:
                for j in range(length):
                    if j % 2 == 0:
                        words_arr[i][j] = words
                words_arr[i][0], words_arr[i][-1] = '#','#'

            if i == 0 or i == 4:
                words_arr[i][0], words_arr[i][-1] = '.','.'

            if i == 1 or i == 3:
                for j in range(1,length,2):
                    words_arr[i][j] = '#'

    else:

        for i in range(5):
            if i % 2 == 0:
                for j in range(0,length,2):
                    words_arr[i][j] = '#'

            if i == 2:
                k = 0
                for j in range(2,length,4):
                    words_arr[i][j] = words[k]
                    k += 1

            if i == 0 or i == 4:
                for j in range(length):
                    words_arr[i][j] ='.'
                for j in range(2,length-2,4):
                    words_arr[i][j] ='#'

            if i == 1 or i == 3:
                for j in range(1,length,2):
                    words_arr[i][j] = '#'

    for i in range(5):
        print(*words_arr[i],sep='')


