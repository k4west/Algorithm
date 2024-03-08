def fibo(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a+b
    return a

print(fibo(int(input())-1))