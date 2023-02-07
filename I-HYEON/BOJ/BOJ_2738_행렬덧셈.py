A,B = map(int,input().split())

board1 = []
for i in range(A):
    board1.append(list(map(int, input().split())))

board2 = []
for i in range(A):
    board2.append(list(map(int, input().split())))

ans = []
for i in range(A):
    temp = []
    for j in range(B):
        temp.append(board1[i][j]+board2[i][j])
    ans.append(temp)

for i in range(A):
    for j in range(B):
        print(ans[i][j],end=" ")
    print()