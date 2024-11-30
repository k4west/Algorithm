from collections import deque
a=iter(open(0).read().split())
t = []
q = deque([])
count = 0
for _ in range(int(next(a))):
    if (op:=next(a).strip()) == 'push':
        q.append(next(a).strip())
        count += 1
    elif op == 'pop':
        if count:
            t.append(q.popleft())
            count -= 1
        else:
            t.append('-1')
    elif op == 'size':
        t.append(str(count))
    elif op == 'empty':
        t.append(str(int(count==0)))
    elif op == 'front':
        if count:
           t.append(q[0])
        else:
            t.append('-1')
    elif op == 'back':
        if count:
            t.append(q[-1])
        else:
            t.append('-1')
print('\n'.join(t))