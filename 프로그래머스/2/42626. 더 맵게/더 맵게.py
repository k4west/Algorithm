from heapq import heappop, heappush, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while (a:=heappop(scoville)) < K:
        if scoville:
            heappush(scoville, a + heappop(scoville)*2)
            answer += 1
        else:
            return -1
    return answer