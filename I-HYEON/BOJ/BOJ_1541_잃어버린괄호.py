string = input() #문자열 입력
lst = string.split('-') # - 부호를 기준으로 스플릿함. 이렇게 하면 리스트 생김.
mini = 0 #최소값을 0으로 초기화

#lst[0]은 더해서 mini에 더해줌
x = sum(map(int,lst[0].split('+')))
mini += x

#lst[1:]는 더해서 mini에서 빼줌
for i in lst[1:]:
    i = sum(map(int,(i.split('+'))))
    mini -= i

print(mini)