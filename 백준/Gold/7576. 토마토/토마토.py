import sys

def f():
    M, N = map(int, sys.stdin.readline().split())
    Box =  []
    for _ in range(N):
        Box.extend(sys.stdin.readline().split())
    ripe = []
    for i, t in enumerate(Box):
        if t=='1':
            ripe.append((i))
    day = -1
    while ripe:
        day += 1
        temp = []
        for t in ripe:
            if t//M > 0 and Box[t-M]=='0':
                Box[t-M] = '1'
                temp.append(t-M)
            if t//M < N-1 and Box[t+M]=='0':
                Box[t+M] = '1'
                temp.append(t+M)
            if t%M > 0 and Box[t-1]=='0':
                Box[t-1] = '1'
                temp.append(t-1)
            if t%M < M-1 and Box[t+1]=='0':
                Box[t+1] = '1'
                temp.append(t+1)
        ripe = temp
    print((day,-1)['0' in Box])
if  __name__ == "__main__":
    f()