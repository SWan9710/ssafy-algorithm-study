T = int(input())
for t in range(T):
    N = int(input())
    stacks = [[], []]
    for _ in range(N):
        start, end = map(lambda x: (int(x)-1)//2, input().split())
        stacks[0].append((start, end) if start < end else (end, start))
    stacks[0].sort(reverse=True)
    idx = cnt = 0
    while 1:
        cnt += 1
        nxt_idx = (idx+1) % 2
        prev = 0
        while stacks[idx]:
            student = stacks[idx].pop()
            if not prev or prev[1] < student[0]: prev = student
            else: stacks[nxt_idx].append(student)
        stacks[nxt_idx].sort(reverse=True)
        if stacks[nxt_idx]: idx = nxt_idx
        else: break
    print(f"#{t+1}", cnt)
