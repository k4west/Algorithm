from collections import deque 
def solution(priorities, location):
    priorities = deque(priorities)
    ans = 1
    while priorities:
        p = priorities.popleft()
        if location > 0:
            location -= 1
            if p < max(priorities):
                priorities.append(p)
            else:
                ans += 1
        elif priorities and p < max(priorities):
            location = len(priorities)
            priorities.append(p)
        else:
            return ans
