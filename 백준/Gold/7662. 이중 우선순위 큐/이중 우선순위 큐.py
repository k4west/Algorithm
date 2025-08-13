from heapq import heappop, heappush

a = open(0)
ans = []
for _ in range(int(next(a))):
    cnt = 0                 # 삽입된 정수 수
    maxQ, minQ = [], []     # 최대/최소 큐
    dct = {}                # 삽입된 정수의 갯수를 관리

    for _ in range(int(next(a))):
        op, n = next(a).split()
        if op == 'I':       # ‘I n’은 정수 n을 Q에 삽입
            n = int(n)      # -2^31 <= n < 2^31
            cnt += 1

            if n in dct:    # 동일한 정수가 삽입될 수 있음
                dct[n] += 1
            else:
                dct[n] = 1
                heappush(maxQ, -n)
                heappush(minQ, n)

        elif cnt:
            if n == '1':                    # ‘D 1’는 Q에서 최댓값을 삭제
                while -maxQ[0] not in dct:   # minQ에서 삭제 된 원소 처리
                    heappop(maxQ)

                cnt -= 1                    # 최댓값 삭제
                x = -maxQ[0]
                if dct[x] == 1:
                    heappop(maxQ)
                    del dct[x]
                else:
                    dct[x] -= 1

            else:                           # ‘D -1’는 Q 에서 최솟값을 삭제
                while minQ[0] not in dct:   # maxQ에서 삭제 된 원소 처리
                    heappop(minQ)

                cnt -= 1                    # 최솟값 삭제
                x = minQ[0]
                if dct[x] == 1:
                    heappop(minQ)
                    del dct[x]
                else:
                    dct[x] -= 1

    if cnt:    # Q에 남아 있는 값 중 최댓값과 최솟값을 출력하라.
        while -maxQ[0] not in dct:  # minQ에서 삭제 된 원소 처리
            heappop(maxQ)

        while minQ[0] not in dct:  # maxQ에서 삭제 된 원소 처리
            heappop(minQ)

        ans.append(f"{-heappop(maxQ)} {heappop(minQ)}")
    else:       # 만약 Q가 비어있다면 ‘EMPTY’
        ans.append("EMPTY")

print("\n".join(ans))
