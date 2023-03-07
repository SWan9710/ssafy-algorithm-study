import sys
input = sys.stdin.readline

N = int(input())
meetings = [tuple(int(i) for i in input().split()) for _ in range(N)]
meetings.sort(key=lambda meeting: meeting[0], reverse=True)
meetings.sort(key=lambda meeting: meeting[1], reverse=True)

met = [meetings.pop()]
while len(meetings):
    meeting = meetings.pop()
    if met[-1][1] <= meeting[0]:
        met.append(meeting)

print(len(met))
