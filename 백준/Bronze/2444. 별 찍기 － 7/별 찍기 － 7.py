n = int(input())
for i in range(2 * n  - 1):
    if i >= n:
        i = 2 * n - i - 2
    print(' ' * (n -1 - i) + '*' * (2 * i + 1))