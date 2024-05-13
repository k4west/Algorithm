a,b,c=map(int,open(0).read().split())
if c<=b:print(-1)
else:print(a//(c-b)+1)