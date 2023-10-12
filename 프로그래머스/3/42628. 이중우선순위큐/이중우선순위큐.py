# 최대 힙, 최소 힙을 각각 생성해서 결과적으로 입력시 두 번 저장, 삭제시 필요하다면 두 번 삭제를 한다.
# 삭제할 때, 진짜 최댓값 또는 최솟값을 삭제하기 위해서 앞서 다른 힙에서 삭제된 정수들을 먼저 삭제한다.
from heapq import heappop, heappush

def solution(operations):
    Qmax, Qmin, d = [], [], {}  # 최대, 최소힙, 정수의 개수 저장하는 딕셔너리 초기화
    cnt = 0   # Q에 남아있는 정수의 개수 : 입력시 +1, 실제 삭제시 -1

    for s in operations:
        op, n = s.split()   # 연산자, 정수 
        
        # 최대 힙, 최소 힙에 각각 주어진 정수 저장, 딕셔너리에 저장된 주어진 정수 개수 저장
        if op == 'I':
            cnt += 1
            n = int(n)
            c = d.get(n, 0)
            if not c:
                heappush(Qmax, -n)
                heappush(Qmin, n)
            d[n] = c + 1

        # Q에 남아있는 정수가 있으면 삭제 실행
        elif cnt:
            cnt -= 1
            if n == '1':
                # Qmin에서 삭제된 정수가 Qmax의 최댓값으로 저장되어 있다면 그런 정수는 모두 삭제
                while not d.get(-Qmax[0], 0): heappop(Qmax)

                # 최댓값이 여러 개 있으면 딕셔너리에서 개수만 줄이고, 1개만 있으면 Qmax에서도 삭제
                m = -Qmax[0]
                c = d.get(m, 0)
                if c:
                    d[m] -= 1
                    if c == 1: heappop(Qmax)
            else:
                # Qmax에서 삭제된 정수가 Qmin의 최솟값으로 저장되어 있다면 그런 정수는 모두 삭제
                while not d.get(Qmin[0], 0): heappop(Qmin)

                # 최솟값이 여러 개 있으면 딕셔너리에서 개수만 줄이고, 1개만 있으면 Qmin에서도 삭제
                m = Qmin[0]
                c = d.get(m, 0)
                if c:
                    d[m] -= 1
                    if c == 1: heappop(Qmin)  

    # 실제 남아있는 최댓값과 최솟값을 구하기 위해서 다른 힙에서 삭제된 정수 삭제
    # 모든 처리 후, 남아 있는 Qmax, Qmin의 최댓값, 최솟값 또는 EMPTY 반환
    if cnt:
        while not d.get(-Qmax[0], 0): heappop(Qmax)
        while not d.get(Qmin[0], 0): heappop(Qmin)
        return [-Qmax[0], Qmin[0]]
    return [0, 0]


if __name__ == "__main__":
    main()
    