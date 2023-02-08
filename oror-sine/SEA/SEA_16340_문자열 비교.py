def boyer_moore(short, long):
    M, N = len(short), len(long)
    l = M-1
    while l < N:
        s = -1
        d = 0
        while long[l] == short[s]:
            if s == -M: return 1
            l -= 1
            s -= 1
        while long[l] != short[s]:
            if s == -M: break
            s -= 1
            d += 1
        l += d
    return 0


T = int(input())
for t in range(T):
    short = input()
    long = input()
    print(f"#{t+1}", boyer_moore(short, long))
