def solution(clothes):
    dic = {}
    for value, key in clothes:
        if dic.get(key):
            dic[key] += [value]
        else:
            dic[key] = [value]

    combination = 1
    for value in dic.values():
        combination *= (len(value) + 1)

    return combination - 1
