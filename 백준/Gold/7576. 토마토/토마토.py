import sys
def f():
    M, N = map(int, sys.stdin.readline().split())
    Box =  [[] for _ in range(N)]
    ripe = []
    for i in range(N):
        Box[i] = sys.stdin.readline().split()
        for j, t in enumerate(Box[i]):
            if t=='1':
                ripe.append((i,j))
    day = -1
    while ripe:
        day += 1
        temp = []
        for t in ripe:
            i, j = t
            if i > 0 and Box[i-1][j]=='0':
                Box[i-1][j] = True
                temp.append((i-1,j))
            if i < N-1 and Box[i+1][j]=='0':
                Box[i+1][j] = True
                temp.append((i+1,j))
            if j > 0 and Box[i][j-1]=='0':
                Box[i][j-1] = True
                temp.append((i,j-1))
            if j < M-1 and Box[i][j+1]=='0':
                Box[i][j+1] = True
                temp.append((i,j+1))
        ripe = temp
    for a in Box:
        if '0' in a:
            print(-1)
            return
    print(day)
if  __name__ == "__main__":
    f()