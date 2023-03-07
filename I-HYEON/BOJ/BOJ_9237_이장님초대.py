N = int(input())
#묘목 심는 날짜 리스트에 받아오기
t = list(map(int,input().split()))

#제일 오래걸리는 순으로 정렬
t.sort(reverse=True)

#심는데 하루가 걸리므로 모든 요소에 1 더해주기
trees = list(map(lambda x:x+1,t))

#심어지기까지 각자 자신의 인덱스만큼 기다려야 하므로 자기자신+인덱스
new_trees = []
for i in range(len(trees)):
    new_trees.append(trees[i]+i)

#마지막 나무가 다 자란 다음날 이장님 초대
print(max(new_trees)+1)