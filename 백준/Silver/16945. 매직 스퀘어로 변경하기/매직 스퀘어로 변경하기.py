from itertools import permutations
a=[*map(int,open(0).read().split())]
def f(t):
    s=0
    for i,j in zip(a,t):
        if (k:=i-j)>0:
            s+=k
        else:
            s-=k
    return s
def g(t):
    return len(set(map(sum,[t[:3],t[3:6],t[6:9],t[::3],t[1::3],t[2::3],t[::4],t[2:7:2]])))==1
m=81
for i in permutations(range(1,10), 9):
    if g(i):
        if m>(t:=f(i)):
            m=t
print(m)