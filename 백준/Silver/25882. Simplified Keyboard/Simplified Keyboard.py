from itertools import zip_longest
def main():
    a=open(0)
    T=[]
    for _ in range(int(next(a))):
        f='1'
        for i, j in zip_longest(*next(a).split(),fillvalue='.'):
            if abs(ord(i) - ord(j)) in (1, 8, 9, 10):f='2'
            elif i!=j:f='3';break
        T.append(f)
    print(*T,sep='\n')
main()