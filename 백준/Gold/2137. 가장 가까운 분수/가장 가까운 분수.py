def check(a, b):
    while b: a, b = b, a%b
    return a == 1
def main():
    a, b = map(int, input().split())
    ans, e = [], 1
    for d in range(2, 32768):
        if d==b: continue
        c = (d*a)//b
        for i in [-1, 0, 1]:
            if not check(c+i, d): continue
            if (e_:=abs(a*d-b*(c+i))/(b*d)) and e_ < e: e, ans = e_, [c+i, d]
    print(*ans)
main()