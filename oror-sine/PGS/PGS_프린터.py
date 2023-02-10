def solution(priorities, location):
    cnt = 1
    while 1:
        if priorities[0] == max(priorities):
            priorities.pop(0)
            if location == 0:
                return cnt
            else:
                cnt += 1
        else:
            priorities.append(priorities.pop(0))
        location += -1 if location else len(priorities)-1
