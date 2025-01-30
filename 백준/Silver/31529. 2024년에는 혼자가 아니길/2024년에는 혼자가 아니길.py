x, y = map(int, input().split())
if x <= y <= 2*x: print((2*x-y)*506)
else: print(-1)