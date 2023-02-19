def max_palindrome(board):
    maxi = 0
    for row in board:
        N = len(row)
        for M in range(N, 0, -1):
            flag = 0
            for i in range(N-M+1):
                for j in range(M//2):
                    if row[i+j] != row[i+M-1-j]:
                        break
                else:
                    if maxi < M:
                        maxi = M
                        flag = 1
            if flag:
                break
    return maxi
 
 
for _ in range(10):
    test_case = input()
    b1 = [input() for _ in range(100)]
    b2 = list(zip(*b1))
    print(f"#{test_case}", max((max_palindrome(b1), max_palindrome(b2))))
