def bi_search(s, e):
    while s <= e:
        m = (s+e)//2
        mm = m*m
        if mm == N:
            return m
        elif mm > N:
            e = m-1
        else:
            s = m+1


ans = []
N = int(input())
print(bi_search(1, N))
