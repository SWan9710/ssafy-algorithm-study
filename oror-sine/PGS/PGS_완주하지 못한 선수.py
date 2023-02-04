from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)  # Counter 시간복잡도 O(n)
    return tuple(answer.keys())[0]

# def solution(participant, completion):
#     achiever = {}
#     for completer in completion:
#         if completer in achiever.keys():
#             achiever[completer] +=1
#         else:
#             achiever[completer] = 1
            
#     answer = ''
#     for runner in participant:
#         if achiever.get(runner,0):
#             achiever[runner] -= 1
#         else:
#             answer = runner
            
#     return answer