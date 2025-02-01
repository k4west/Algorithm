def main():
    def change(i):
        switches[i] ^= 1
    
    
    def multiple(n, m):
        for i in range(n-1, m, n):
            change(i)


    def symmetry(n, m):
        count = 1
        switches[n] ^= 1
        while count <= n < m-count and switches[n+count] == switches[n-count]:
            change(n-count)
            change(n+count)
            count += 1
    
    a = open(0)
    m = int(next(a))
    *switches, = map(int, next(a).split())
    
    for _ in range(int(next(a))):
        gender, number = map(int, next(a).split())
        if gender == 1: multiple(number, m)
        else: symmetry(number-1, m)
    
    print('\n'.join(' '.join(map(str, switches[20*i:20*i+20])) for i in range((m+19)//20)))

    
main()