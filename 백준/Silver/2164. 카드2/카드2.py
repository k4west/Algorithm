import sys
n = int(sys.stdin.readline())
li = [i for i in range(1, n+1)]
while len(li)!=1:
    m = len(li)%2
    li = li[1::2]
    if m:
        li.insert(0,0)
print(li[0])