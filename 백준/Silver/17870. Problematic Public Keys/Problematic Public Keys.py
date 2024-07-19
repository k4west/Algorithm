def get_p(n):
    n=int(n)
    for i in range(2, int(n*.5)+1):
        if n%i==0:
            return i, n//i
def main():
    m,*a=open(0)
    p=set()
    for i, j in map(get_p, a):
        p.add(i)
        p.add(j)
    p=sorted(p)
    print('\n'.join([' '.join(map(str, p[5*i:5*i+5])) for i in range(len(p)//5+1)]))
main()