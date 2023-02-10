def solution(nums):
    l = len(nums)//2
    s = len(set(nums))
    answer = l if l < s else s
    return answer
