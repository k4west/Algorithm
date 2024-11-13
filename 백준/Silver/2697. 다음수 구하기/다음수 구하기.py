t = []
for A in open(0).read().split()[1:]:
    flag = False
    B = [A[-1]]
    for i in range(2, len(A)+1):
        n = A[-i]
        if B[-1] > n:
            B.append(n)
            flag = True
            break
        B.append(n)
    if flag:
        m = min([j for j in B if j > n])
        B.sort()
        B.remove(m)
        t.append(A[:-i]+m+''.join(B))
    else:
        t.append('BIGGEST')
print('\n'.join(t))