T = int(input())
for tc in range(T):
    R, S = input().split()
    R = int(R)

    for i in range(len(S)):
        for j in range(R):
            print(S[i],end='')
    print()


