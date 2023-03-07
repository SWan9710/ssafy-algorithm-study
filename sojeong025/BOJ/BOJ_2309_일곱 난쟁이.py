height = [0]*9
for i in range(9):
    height[i] = int(input())

# 버블 정렬 이용해서 오름차순으로 정렬
for j in range(len(height)-1,0,-1):
    for k in range (0,j):
        if height[k] > height[k+1]:
            height[k],height[k+1] = height[k+1], height[k]

# 반복문을 수행하여 전체 합에서 100이 아닌 변수 제거하기
for l in height:
    for m in height:
        if sum(height) -l -m == 100 :
            height.remove(l)
            height.remove(m)
    

for hei in height:
    print(hei)


