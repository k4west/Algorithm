import sys
input = sys.stdin.readline

A = []
while True:
    n = list(list(map(str,input().split()))[0])
    if n == ['0']:
        break
    A.append(n)
    
def yesorno(k):
    if any(i[t] != i[-t - 1] for t in range(k)):
        print('no')
    else:
        print('yes')

for i in A:
    l = len(i)
    if l % 2 == 1:
        l -= 1
    yesorno(int(l/2))