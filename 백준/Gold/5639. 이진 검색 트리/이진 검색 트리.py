import sys
sys.setrecursionlimit(10000*2)

li = []
while True:
    try:
        li.append(int(sys.stdin.readline()))
    except:
        break

def f(s, e):
    if s >= e: 
        print(li[s])
        return
    if li[s] > li[e] or li[s] < li[s+1]:
        f(s+1, e)
        print(li[s])
        return
    for i in range(s+1, e+1):
        if li[s] < li[i]:
            f(s+1, i-1)
            f(i, e)
            break
    print(li[s])

f(0, len(li)-1)