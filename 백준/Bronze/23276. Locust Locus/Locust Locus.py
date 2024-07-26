def gcd(a, b):
    while b:
        a, b= b, a%b
    return a

def main():
    n, *m = map(int, open(0).read().split())
    s = 11723
    for i in range(n):
        y, c1, c2 = m[3*i:3*i+3]
        if s > (t:=y + c1*c2//gcd(c1, c2)):
            s = t
    print(s)
main()