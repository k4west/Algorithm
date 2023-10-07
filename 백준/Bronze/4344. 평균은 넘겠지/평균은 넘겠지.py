import sys
def round3(n):
    if (n*10000)%10 < 5:
        sn = str(n).split('.')
        return sn[0] + "." + sn[1][:3].ljust(3, '0') + '%'
    sn = str(n+0.001).split('.')
    return sn[0] + "." + sn[1][:3] + '%'

C = int(sys.stdin.readline())
li = []
for _ in range(C):
    n, *scores = map(int, sys.stdin.readline().rstrip().split())
    avg = sum(scores)/n
    m = 0
    for score in scores:
        if score > avg: m += 1
    li.append(round3(100*m/n))
print("\n".join(li))