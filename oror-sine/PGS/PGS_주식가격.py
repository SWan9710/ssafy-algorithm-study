def solution(prices):
    answer = []
    length = len(prices)
    for i in range(length):
        price = prices[i]
        cnt = 0
        i += 1
        while i < length:
            cnt += 1
            if prices[i] < price:
                break
            else:
                i += 1
        answer.append(cnt)
    return answer
