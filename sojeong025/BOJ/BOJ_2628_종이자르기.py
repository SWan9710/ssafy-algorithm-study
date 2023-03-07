import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
paper = [[0] * N for _ in range(M)]
row = [0, N]
col = [0, M]

cut = int(input())
for _ in range(cut):
    rc, line = map(int, input().split())
    if rc == 1:
        row.append(line)
    elif rc == 0:
        col.append(line)

row.sort()
col.sort()
row_d = []
col_d = []
for i in range(len(row)-1):
    row_d.append(row[-i-1]-row[-i-2])
for i in range(len(col)-1):
    col_d.append(col[-i-1]-col[-i-2])
print(max(row_d) * max(col_d))


