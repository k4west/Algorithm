import sys
input=sys.stdin.readline
a=int(input())+1
b=set(range(1,a))-set(map(int,input().split()))
print(min(b) if b else a)