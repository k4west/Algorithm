import sys
input=lambda:map(int,sys.stdin.readline().split())
while True:
    a,b,c,d=input()
    if a==0:break
    if a<b:a,b=b,a
    if c<d:c,d=d,c
    print(f'{min(100,max(1,min(c*100//a,d*100//b)))}%')