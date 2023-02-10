def solution(bridge_length, weight, truck_weights):
    queue = [[truck, 0] for truck in truck_weights]
    seconds = 0
    while len(queue):
        if queue[0][1] == bridge_length:
            del queue[0]
        limit = weight
        idx = 0
        while idx < len(queue):
            truck_weight, s = queue[idx]
            if limit >= truck_weight and (idx == 0 or s+1 < queue[idx-1][1]):
                limit -= truck_weight
                queue[idx][1] += 1
                idx += 1
            else:
                break
        seconds += 1
    return seconds
