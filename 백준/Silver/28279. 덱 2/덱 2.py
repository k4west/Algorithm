from collections import deque

def main():
    a = open(0)
    arr = deque([])
    count = 0
    t = []
    for _ in range(int(next(a))):
        i, *n = next(a).strip().split()
        if i == '1':
            arr.appendleft(n[0])
            count += 1
        elif i == '2':
            arr.append(n[0])
            count += 1
        elif i == '3':
            if count:
                t.append(arr.popleft())
                count -= 1
            else:
                t.append('-1')
        elif i == '4':
            if count:
                t.append(arr.pop())
                count -= 1
            else:
                t.append('-1')
        elif i == '5':
            t.append(str(count))
        elif i == '6':
            t.append('10'[bool(count)])
        elif i == '7':
            t.append(arr[0] if count else '-1')
        elif i == '8':
            t.append(arr[-1] if count else '-1')
    print('\n'.join(t))

main()