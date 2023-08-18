n=int(input())
i=int((2*n)**0.5)
i+=int(n>(i*(i+1))//2)
d = n - (i*(i-1))//2 - 1
if i % 2 == 0:
    print(f"{d+1}/{i-d}")
else:
    print(f"{i-d}/{d+1}")