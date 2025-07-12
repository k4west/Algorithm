N = int(input())
g = 0
for n in range(max(1, N-54), N):
    x = t = n
    while n:
        x += n%10
        n //= 10
    if x == N:
        g = t
        break
print(g)