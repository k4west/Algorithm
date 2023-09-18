li = list(map(int, input().split()))
s = sum(li)
c = 2*max(li)-s
if c>=0:
    print(s-c-1)
else:
    print(s)