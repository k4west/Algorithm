def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def main():
    n = int(input())
    t = {(0, 1), (1, 1)}
    for i in range(1, n+1):
        for j in range(1, i):
            d = gcd(i, j)  
            t.add((j//d, i//d))
    s = [(j, i) for j, i in t]
    s.sort(key=lambda x: x[0]*n/x[1])
    print(len(s))
    print('\n'.join(map(lambda x: f'{x[0]}/{x[1]}', s)))
main()