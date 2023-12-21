from collections import deque

def solution(plans):
    answer, task, paused = [], [], []
    
    for name, start, duration in plans:
        h, m = map(int, start.split(':'))
        task.append((h*60+m, int(duration), name))
    task = deque(sorted(task))
    
    while task:
        s0, d0, n0 = task.popleft()
        if task:
            s1 = task[0][0]
            if (e:=s0+d0) <= s1:
                answer.append(n0)
                while paused:
                    if e+(t:=paused[-1][1]) <= s1:
                        e += t
                        answer.append(paused.pop()[0])
                    else:
                        paused[-1][1] -= s1-e
                        break
            else:
                paused.append([n0, e-s1])
        
    answer.append(n0)
    answer.extend([n for n, t in paused[::-1]])
    
    return answer