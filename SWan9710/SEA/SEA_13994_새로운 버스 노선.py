import sys
sys.stdin=open('input.txt')

# 모든 버스는 A번에서 출발해 B번까지 운행하므로, A와 B 정류장에서 반드시 정차한다.
# 일반버스는 A번부터 B번 사이의 모든 정류장에 정차한다.

# 급행버스는 A가 짝수인 경우 A와 B 사이의 모든 4의 배수 번호 정류장에,
# A가 홀수인 경우 A와 B 사이의 모든 홀수 번호 정류장에 정차한다.

# 광역 급행 버스는 A가 짝수인 경우 A와 B의 4의 배수 번호 정류장에
# A가 홀수인 경우 A 와 B 사이의 3의 배수 이면서 10의 배수가 아닌 번호 정류장에 정차한다.

# 첫째줄 테스트 케이스
# 둘째줄 노선의 수
# N개의 줄마다 각각 다른 번호의 버스 타입
# 1 일반, 2 급행, 3 광역 급행
# 버스 번호 후 A 정류장 B 정류장 공백띄고 주어짐

test_case = int(input())
for tc in range(1, test_case+1):
    N = int(input())

    # 정류장은 1번부터 1000번까지 존재
    bus_arr = [0] * 1001

    for n in range(N):
        bus_information, A, B = map(int, (input().split()))
        # 결과값을 저장할 공간


        # 일반버스 일때
        if bus_information == 1:
            for i in range(A, B+1):
                bus_arr[i] += 1

        # 급행버스 일때
        if bus_information == 2:
            for i in range(A, B + 1):
                # 짝수일때
                if A % 2 == 0:
                    if i % 2 == 0:
                        bus_arr[i] += 1

                # 홀수일때
                elif A % 2 == 1:
                    if i % 2 == 1:
                        bus_arr[i] += 1

        # 광역급행버스 일때
        if bus_information == 3:
            for i in range(A, B + 1):
                # 짝수일때
                if A % 2 == 0:
                    if i % 4 == 0:
                        bus_arr[i] += 1

                # 홀수일때
                elif A % 2 == 1:
                    if i % 3 == 0 and i % 10 != 0:
                        bus_arr[i] += 1

    # 버블 소트로 정렬해줌
    for i in range(len(bus_arr)-1, -1, -1):
        for j in range(i):
            if bus_arr[j] > bus_arr[j+1]:
                bus_arr[j], bus_arr[j+1] = bus_arr[j+1], bus_arr[j]

    print(f'#{tc} {bus_arr[-1]}')



