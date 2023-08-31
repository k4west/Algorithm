import sys
a, b = map(int, sys.stdin.readline().split())
if a == b:
    print("{:.3f}".format(round(1-(10-a)/153, 3)))
else:
    li = list(range(1,11))*2
    li.remove(a)
    li.remove(b)
    a = (a+b)%10
    s = 0
    for i in range(18):
        for j in range(i+1, 18):
            if li[i] != li[j] and (li[i]+li[j])%10 < a:
                s += 1 
    print("{:.3f}".format(round(s/153, 3)))