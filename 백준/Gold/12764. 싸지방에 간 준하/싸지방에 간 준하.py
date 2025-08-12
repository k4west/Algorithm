from heapq import heappop, heappush


N = int(input())    # 1 <= 사람 수 <= 100000
info = [[*map(int, input().split())] for _ in range(N)]
info.sort()

computers = []    # (끝나는 시간, 컴퓨터 순번)
acc_user = [0]*N  # 누적 이용자 수
cnt = 0           # 설치 컴퓨터 수
buf = []          # 사용 가능한 컴퓨터 index

for p, q in info:
    while computers and p >= computers[0][0]:
        e, c = heappop(computers)
        heappush(buf, c)
    
    if buf:                             # 시작 가능한 컴퓨터가 있으면
        c = heappop(buf)
        heappush(computers, (q, c))     # 사용 기록
        acc_user[c] += 1                # 누적 이용자 수 기록

    else:                               # 지금 시작 가능 x
        heappush(computers, (q, cnt))   # 사용 기록
        acc_user[cnt] += 1              # 누적 이용자 수 기록
        cnt += 1                        # 컴퓨터 증설 기록

print(cnt)
print(" ".join(map(str, acc_user[:cnt])))
