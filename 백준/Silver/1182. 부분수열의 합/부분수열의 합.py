import sys
input = sys.stdin.readline

N, S = map(int, input().split())
*arr, = map(int, input().split())

c = 0
if not S: c = -1

def f(s, a):
    global c
    
    if s == S: 
        c += 1
    
    for i in range(a+1, N):
        s += arr[i]
        f(s, i)
        s -= arr[i]

f(0, -1)

print(c)