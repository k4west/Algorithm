s='*.'
n,m=map(int,input().split())
print('\n'.join(''.join(s[(i+j)%2] for i in range(m)) for j in range(n)))