import sys
text = sys.stdin.readline().strip()
lst = []

for i in range(1, len(text)):
    for j in range(i+1, len(text)):
        lst.append(text[i-1::-1]+text[j-1:i-1:-1]+text[len(text)-1:j-1:-1])

print(sorted(lst)[0])
