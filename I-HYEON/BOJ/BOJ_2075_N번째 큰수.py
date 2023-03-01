import heapq  # 힙 모듈에서 heappop은 힙에서 최소값을 pop해주므로 이를 이용

heap = []  # 힙 생성
N = int(input())

for _ in range(N):  # N 줄 만큼 반복
    nums = map(int,input().split())  # 입력 숫자를 nums 에 받아와서
    for num in nums:  # for문으로 입력 숫자를 순회

        if len(heap) < N:  # 힙의 크기를 N으로 고정시키기 위한 조건(N번째로 큰 수를 구하기 위해)
            heapq.heappush(heap,num)  # 힙 크기가 N이 안되면 push
        
        else:  # 힙 크기가 N이면 힙의 최소값과 숫자를 비교해 더 큰 수를 넣음. 이를 반복하면 힙안에는 최대값 N개가 들어가게 됨.
            key = heapq.heappop(heap)  # heappop한 값을 key에 담아 비교
            if key < num:  # 더 큰 쪽을 다시 힙에 넣어줌.
                heapq.heappush(heap,num)
            else:
                heapq.heappush(heap,key)

print(heap[0])  # 최종적으로 완성된 힙에서 제일 작은 값이 N번째로 큰 수
