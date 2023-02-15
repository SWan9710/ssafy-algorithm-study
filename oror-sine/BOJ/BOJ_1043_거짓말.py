import sys
N, M = map(int, sys.stdin.readline().split())

isdetector = 0
detectors = []
for i in sys.stdin.readline().split():
    if detectors:
        detector = int(i)-1
        isdetector += (1 << detector)
        detectors.append(detector)
    else:
        detectors.append(int(i))

def cnt_detector_in(party):
    global isdetector
    cnt = 0
    for i in range(1, party[0]+1):
        if isdetector & (1 << party[i]):
            cnt += 1
    party[-1] = cnt
    return cnt

parties = []
for _ in range(M):
    party = []
    for i in sys.stdin.readline().split():
        party.append(int(i)-1 if party else int(i))
    party.append(0)
    cnt_detector_in(party)
    parties.append(party)

def tell_truth():
    global parties
    global isdetector
    parties.sort(key=lambda x:(cnt_detector_in(x), -x[0]))
    if parties and parties[-1][-1]:
        while parties and parties[-1][-1]:
            for i in range(1, parties[-1][0]+1):
                if not(isdetector & 1 << parties[-1][i]):
                    isdetector += (1 << parties[-1][i])
            parties.pop()
        tell_truth()

tell_truth()
print(len(parties))