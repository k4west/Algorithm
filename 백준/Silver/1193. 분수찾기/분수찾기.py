def s(i):
    return (i*(i+1))//2
n=int(input())
i=int((2*n)**0.5)
while True:
    if s(i-1)< n <= s(i):
        d = n - s(i-1) - 1
        if i % 2 == 0:
            print(f"{d+1}/{i-d}")
            break
        else:
            print(f"{i-d}/{d+1}")
            break
    i += 1