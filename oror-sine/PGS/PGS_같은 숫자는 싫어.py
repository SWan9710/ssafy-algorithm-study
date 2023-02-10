def solution(arr):
    lst = [arr[0]]
    for i in arr[1:]:
        if lst[-1] != i:
            lst.append(i)
    return lst
