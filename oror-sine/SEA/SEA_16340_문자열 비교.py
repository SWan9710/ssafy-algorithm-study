def boyer_moore(pattern, text):
    P, T = len(pattern), len(text)
    t = P
    while t <= T:
        p = dt = -1
        while -P <= p and pattern[p] == text[t+dt]:
            p -= 1
            dt -= 1
        if p < -P:
            return 1

        jump = 0
        while -P <= p and pattern[p] != text[t+dt]:
            jump += 1
            p -= 1
        t += jump

    return 0

T = int(input())
for t in range(T):
    pattern = input()
    text = input()
    print(f"#{t+1}", boyer_moore(pattern, text))
