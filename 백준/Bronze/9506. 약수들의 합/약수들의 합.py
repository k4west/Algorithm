from sys import stdin
while True:
    N = int(stdin.readline())
    if N == -1:
        break
    t = N
    s = f"{N} = 1"
    for i in range(2, N//2+1):
        if N % i == 0:
            s += f" + {i}"
            t -= i
    if t == 1:
        print(s)
    else:
        print(f"{N} is NOT perfect.")