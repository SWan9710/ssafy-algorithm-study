# 10개의 숫자가 주어지는데 전부 42로 나눴을 때 나오는
#나머지의 종류를 구해야함
#겹치는 숫자는 하나로 봐야하니까 set이용?
#하나씩 돌리면서 나머지를 구하고 set에 추가하면 되려나

myset = set()

for i in range(10):
    myset.add(int(input())%42)

print(len(myset))