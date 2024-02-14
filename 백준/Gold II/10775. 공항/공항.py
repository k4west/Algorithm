import sys
sys.setrecursionlimit(10**6)
input = lambda: int(sys.stdin.readline())
roots = [i for i in range(input() + 1)]
def find_root(x):
    if x == (t := roots[x]): return x
    else: roots[x] = find_root(t)
    return roots[x]
a = 1
for i in range((input())):
    if (t:=find_root(g:=input())): roots[t] = t - 1
    else: a = 0; break
print(i+a)