from heapq import heappop, heappush, heapify
def solution(jobs):
    jobs.sort()
    n = len(jobs)
    ans = now = 0
    for _ in range(n):
        tmp = []
        for i, (asked, required) in enumerate(jobs):
            if asked > now: break
            heappush(tmp, (now + required, i))
        if tmp:
            _, idx = heappop(tmp)
            asked, required = jobs.pop(idx)
        else:
            asked, required = jobs.pop(0)
            now = asked
        now += required
        ans += now - asked
    return ans // n