cnt = int(input())
mylist = list(map(int,input().split()))

max_score = max(mylist)
mylist = list(map(lambda x: x/max_score*100,mylist))

ans = sum(mylist)/cnt
print(ans)