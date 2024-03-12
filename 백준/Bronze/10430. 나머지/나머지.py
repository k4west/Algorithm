A, B, C = map(int, input().split())
n, m = (A+B)%C, (A*B)%C
print('\n'.join(map(str, [n, n, m, m])))