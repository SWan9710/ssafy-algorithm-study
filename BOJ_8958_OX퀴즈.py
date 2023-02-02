T = int(input())
for i in range(T):
    ox = input()
    score_list = []
    score = 0
    for j in range(len(ox)):
        if ox[j] == 'O':
            score += 1
            score_list.append(score)
        else:
            score = 0
    print(sum(score_list))