a = open(0)
for i in a:
    n, *arr = map(int, i.split())
    if set(range(1, n)) - set(abs(arr[i] - arr[i-1]) for i in range(1, n)): print('Not jolly')
    else: print('Jolly')