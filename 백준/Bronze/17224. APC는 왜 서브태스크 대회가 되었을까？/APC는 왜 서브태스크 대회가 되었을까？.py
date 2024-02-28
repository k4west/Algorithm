import sys
input = lambda: map(int, sys.stdin.readline().split())
N, L, K = input()
scores={100: 0, 140: 0}
for _ in range(N):
    sub1,sub2=input()
    if sub2<=L:scores[140]+=1
    elif sub1<=L:scores[100]+=1
a,b=scores[140],scores[100]
if a>K:a,b=K,0
elif a+b>K:b=K-a
print(a*140+b*100)