n = int(input())
m = 2*n-1
for i in range(m):
    if i < n: print(('*'*(2*(n-i)-1)).center(m).rstrip())
    else: print(('*'*(2*(i-n)+3)).center(m).rstrip())