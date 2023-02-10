def func(progress, speed):
    def wrapper(t):
        return progress + speed*t
    return wrapper


def solution(progresses, speeds):
    queue = []
    for progress, speed in zip(progresses, speeds):
        queue.append(func(progress,speed))
    answer = []
    t = 1
    while len(queue):
        cnt = 0
        while len(queue) and queue[0](t) >= 100:
            cnt += 1
            del queue[0]
        if cnt:
            answer.append(cnt)
        t += 1

    return answer
