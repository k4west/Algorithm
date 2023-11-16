from collections import deque
def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    goal = sum1 + sum2
    
    if goal % 2:
        return -1
    
    goal //= 2
    count = 0
    n = len(queue1) + len(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while goal != sum1:
        if count >= n:
            return -1
        while sum1 > goal:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            count += 1
        while sum1 < goal:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            count += 1
    return count