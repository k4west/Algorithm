from collections import deque
def solution(progresses, speeds):
    days = deque([(100-p)//s + int(bool((100-p)%s)) for p, s in zip(progresses, speeds)])
    ans = [1]
    prev = days.popleft()
    while days:
        now = days.popleft()
        if prev >= now:
            ans[-1] += 1
        else:
            ans.append(1)
            prev = now
    return ans