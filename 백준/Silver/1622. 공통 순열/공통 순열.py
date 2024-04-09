import sys
li = sys.stdin.readlines()
ans = []
s = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0, len(li), 2):
    a, b = li[i], li[i+1]
    t = ""
    for i in s:
        t += i*min(a.count(i), b.count(i))
    print(t)