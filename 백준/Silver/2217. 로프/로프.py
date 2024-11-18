a = open(0)
N = int(next(a))
ropes = sorted(map(float, a.read().split()))
m = 0
for i in range(N):
    if m < (t:=ropes[i]*(N-i)):
        m = t
print(int(m))