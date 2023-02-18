import sys
input = sys.stdin.readline

N = int(input())        
T = list(map(int, input().split()))    
T.sort(reverse=True)

for i in range(N):
    T[i] += i + 1

T.sort(reverse=True)
print(T[0]+1)

# count = 0
# while True:
#     for i in range(len(T)):
#         if T[i] == 0:
#             continue
#         T[i] -= 1
#     count += 1
#     if len(set(T)) == 1:
#         break
# print(count+1)