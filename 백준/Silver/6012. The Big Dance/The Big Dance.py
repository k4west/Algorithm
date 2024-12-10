def f(s, e):
    if e-s<=2:
        return s**2+s
    else:
        m = (s+e)//2
        return f(s, m) + f(m+1, e)

def main():
    n = int(input())
    print(f(1, n))
    
main()