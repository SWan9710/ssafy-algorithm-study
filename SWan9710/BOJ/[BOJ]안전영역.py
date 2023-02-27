dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(i, j):
    stack = [(i,j)]
    visited[i][j] = 0
    while stack:
        sx, sy = stack.pop()
        for k in range(4):
            nx, ny = sx + dx[k], sy + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] > visited[sx][sy]:
                    stack.append((nx,ny))
                    visited[nx][ny] = 0

# 배열크기 입력받기
N = int(input())
# 배열정보 입력받기
arr = [list(map(int, input().split())) for _ in range(N)]
# 배열정보를 토대로 원본을 해치지않을 새로운 배열 생성
visited = [[0] * N for _ in range(N)]
# 결과를 비교하여 출력해줄 result 변수
result = 0
# arr의 최고값 저장
high = max(max(arr))
# while 문을 돌며 종료조건 과 비가오는 횟수를 저장하기 위한 rain 변수
rain = 0
while rain != high:
    for i in range(N):
        for j in range(N):
            # 비가 왔을때 땅의 높이
            visited[i][j] = arr[i][j] - rain

    # 시작지점 가져오기
    count = 0
    # 시작지점은 아직 침수되지 않은 땅부터 시작해줄거
    for i in range(N):
        for j in range(N):
            if visited[i][j] > 0:
                # 반복문을 돌며 침수되지 않은 땅을 찾는데 상하좌우로 연결되어 있어야 이동이 가능
                # 만약 끊긴다면 조건문이 맞지 않으므로 함수가 종료될거고 다시 바뀐 배열을 토대로
                # 시작지점을 다시 찾아서 함수를 돌릴거
                # 이렇게 반복하면 연결되어 있는 땅덩이들의 갯수가 나옴
                count += 1
                DFS(i, j)
    # 그 값이 현재 저장되어 있는 result 보다 크면 초기화 해줄거
    if result < count:
        result = count

    # 비는 모든 꼭대기를 물에 잠기게 할때까지 돌거
    rain += 1
print(result)