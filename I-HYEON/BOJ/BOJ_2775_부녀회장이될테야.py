T= int(input())

for tc in range(T):
    k = int(input())
    n = int(input())

    def apart(k,n):
        if k == 0:
            return n
        people = 0
        for j in range(1,n+1):
            people += apart(k-1,j)
        return people

    print(apart(k,n))