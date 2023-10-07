import sys
N = list(sys.stdin.readline().rstrip())
if len(N) == 1: N.insert(0,'0')
N = list(map(int, N))
tmp = [N[1], sum(N)%10]
c = 1
while tmp != N:
    tmp = [tmp[1], sum(tmp)%10]
    c += 1
print(c)