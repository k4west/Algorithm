# 최대 힙, 최소 힙을 각각 생성해서 결과적으로 입력시 두 번 저장, 삭제시 두 번 삭제를 한다.
# 입력할 때, 정수와 함께 주어진 입력 순번도 함께 저장
# 삭제할 때, 앞서 다른 힙에서 삭제된 정수들을 삭제하고, 최댓값 또는 최솟값을 삭제한다.
# 다른 힙에서 삭제한 정수의 정보는 삭제시 입력 순번을 기준으로 표시된 방문 기록으로 확인 한다
import sys
import heapq

li = [] # 최종 출력물 저장할 리스트

for _ in range(int(sys.stdin.readline())):
    # 최대, 최소힙, 방문 기록 초기화
    Qmax, Qmin = [], []
    visited = [False] * 10**6

    for i in range(int(sys.stdin.readline())):  # i : 입력 순번
        # 연산자와 정수 입력받기
        op, n = sys.stdin.readline().rstrip().split()

        # 최대 힙, 최소 힙에 각각 정수와 입력 순번 저장
        if op == 'I':
            n = int(n)
            heapq.heappush(Qmax, (-n, i))
            heapq.heappush(Qmin, (n, i))
            
        # 다른 힙에서 삭제된 정수를 입력 순번을 통해 확인해서 삭제해준 뒤,
        # Q에 정수가 남아 있으면, 입력 순번으로 방문 표시 후 1과 -1에 따라서 최댓값, 최솟값 삭제 후
        else:
            if n == '1':
                while Qmax and visited[Qmax[0][1]]:
                    heapq.heappop(Qmax)
                if Qmax:
                    visited[Qmax[0][1]] = True
                    heapq.heappop(Qmax)
            else:
                while Qmin and visited[Qmin[0][1]]:
                    heapq.heappop(Qmin)
                if Qmin:
                    visited[Qmin[0][1]] = True
                    heapq.heappop(Qmin)
    
    # 다른 힙에서 삭제된 정수를 마저 삭제하는 과정
    while Qmax and visited[Qmax[0][1]]:
        heapq.heappop(Qmax)
    while Qmin and visited[Qmin[0][1]]:
        heapq.heappop(Qmin)

    # 모든 연산 처리 후, 남아 있는 Qmax, Qmin의 최댓값, 최솟값 저장 또는 EMPTY 저장
    if Qmax : li.append(" ".join(map(str, (-Qmax[0][0], Qmin[0][0]))))
    else: li.append("EMPTY")

print("\n".join(li))    # 출력