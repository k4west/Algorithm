from heapq import heappop, heappush

N = int(input())    # 사람 수 1 <= N <= 100,000
info = [tuple(map(int, input().split())) for _ in range(N)]  # 이용 시작 시각과 종료 시각 정보
info.sort()

cnt = 0
computers = []
available = []      # 사용 가능한 컴퓨터 목록
acc_user = [0]*N    # 누적 이용자 수 기록용 리스트

for p, q in info:
    while computers and p >= computers[0][0]:    # 다음 방문자가 사용할 수 있는 컴퓨터가 있으면
        e, idx = heappop(computers)
        heappush(available, idx)  # 사용 가능한 컴퓨터 인덱스 추가

    if available:                   # 사용 가능한 컴퓨터 중에
        idx = heappop(available)    # 번호가 가장 작은 컴퓨터
    else:
        idx = cnt
        cnt += 1

    heappush(computers, (q, idx))  # 새로운 사용자 컴퓨터 사용 기록
    acc_user[idx] += 1  # 사용자 수 누적 기록

print(cnt)  # 컴퓨터의 최소 개수
print(" ".join(map(str, acc_user[:cnt])))    # 자리 별로 이용한 사람 수
