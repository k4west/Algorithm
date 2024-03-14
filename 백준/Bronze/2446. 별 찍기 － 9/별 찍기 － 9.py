n = int(input())
m = 2*n-1
for i in range(m):
    if i < n: print(('*'*(2*(n-i)-1)).rjust(2*n-i-1))
    else: print(('*'*(2*(i-n)+3)).rjust(i+1))