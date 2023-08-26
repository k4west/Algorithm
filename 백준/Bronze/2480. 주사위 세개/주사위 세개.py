li = list(map(int, input().split()))
s = set(li)
if len(s) == 3:
    print(max(li)*100)
elif len(s) == 1:
    print(10000+li[0]*1000)
else:
    print(1000+(sum(li)-sum(list(s)))*100)