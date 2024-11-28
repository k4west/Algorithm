from collections import deque

def main():
    a = open(0)
    arr = deque([])
    count = 0
    t = []
    for _ in range(int(next(a))):
        i, *n = next(a).strip().split()
        if i == '1':
            arr.appendleft(int(n[0]))
            count += 1
        elif i == '2':
            arr.append(int(n[0]))
            count += 1
        elif i == '3':
            if count:
                t.append(arr.popleft())
                count -= 1
            else:
                t.append(-1)
        elif i == '4':
            if count:
                t.append(arr.pop())
                count -= 1
            else:
                t.append(-1)
        elif i == '5':
            t.append(count)
        elif i == '6':
            t.append(int(not bool(count)))
        elif i == '7':
            t.append(arr[0] if count else -1)
        elif i == '8':
            t.append(arr[-1] if count else -1)
    print('\n'.join(map(str, t)))

main()