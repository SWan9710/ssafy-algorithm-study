import heapq

def solution(jobs):
    heapq.heapify(jobs)
    N = len(jobs)
    queue = []

    time_taken = t = remaining = ongoing = 0

    while jobs or queue or ongoing:
        while jobs and jobs[0][0] == t:
            req, duration = heapq.heappop(jobs)
            heapq.heappush(queue,(duration, req))

        if not ongoing and queue:
            ongoing = heapq.heappop(queue)
            remaining = ongoing[0]
        
        if not ongoing and not queue:
            t = jobs[0][0]
        else:
            t += 1
            remaining -= 1
            if ongoing and remaining <= 0:
                time_taken += t - ongoing[1]
                ongoing = 0
                
    return time_taken//N
