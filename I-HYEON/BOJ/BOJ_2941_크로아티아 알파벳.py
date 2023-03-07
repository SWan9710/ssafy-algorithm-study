# 크로아티아 알파벳을 변경한 문자를 담은 리스트를 만든다.
# 문자열을 입력받는다.
# 리스트를 돌면서 문자열 내에 해당 문자가 있으면 'a'로 변경하고, 그때마다 재할당함.
# 최종적으로 변경된 문자열의 길이를 반환한다.

string = input()
croa_li = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croa_li:
    string = string.replace(i,'a')

print(len(string))