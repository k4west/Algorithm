def sub(i, j, k, s):
    if j+k == L:
        if j >= 1 and k >= 2:
            ans.append(s)
        return
    
    t = S[i]
    dj = t in 'aeiou'
    dk = not dj
    sub(i+1, j+dj, k+dk, s+t)
    
    if C - i > L - (j+k):
        sub(i+1, j, k, s)


ans = []
L, C = map(int, input().split())
S = input().split()
S.sort()
sub(0, 0, 0, "")
print("\n".join(ans))